from ...dao import db
from ..lesson.models import AILesson
from .dtos import ChapterDto
from sqlalchemy import func
from ...util.uuid import generate_id
from ..common.models import raise_error
from ..lesson.const import (
    LESSON_TYPE_TRIAL,
    STATUS_PUBLISH,
    STATUS_DRAFT,
    STATUS_DELETE,
    STATUS_HISTORY,
    STATUS_TO_DELETE,
)
from datetime import datetime
from .dtos import SimpleOutlineDto
from .utils import get_existing_outlines, get_existing_blocks
from flaskr.service.check_risk.funcs import check_text_with_risk_control


# get chapter list
# @author: yfge
# @date: 2025-04-14
# get chapter list will return the chapter list of the scenario
# is used for the scenario outline page in the cook-web
def get_chapter_list(app, user_id: str, scenario_id: str):
    with app.app_context():
        outlines = get_existing_outlines(app, scenario_id)
        chapters = [o for o in outlines if len(o.lesson_no) == 2]
        return [
            ChapterDto(
                chapter.lesson_id,
                chapter.lesson_name,
                chapter.lesson_desc,
                chapter.lesson_type,
            )
            for chapter in chapters
        ]


# create chapter
def create_chapter(
    app,
    user_id: str,
    scenario_id: str,
    chapter_name: str,
    chapter_description: str,
    chapter_index: int = 0,
    chapter_type: int = LESSON_TYPE_TRIAL,
):
    with app.app_context():
        existing_chapter = AILesson.query.filter(
            AILesson.course_id == scenario_id,
            AILesson.status.in_([STATUS_PUBLISH, STATUS_DRAFT]),
            AILesson.lesson_name == chapter_name,
        ).first()
        if (
            existing_chapter
            and AILesson.query.filter(
                AILesson.course_id == scenario_id,
                AILesson.status.in_([STATUS_TO_DELETE, STATUS_DELETE]),
                AILesson.lesson_name == chapter_name,
            ).first()
            is None
        ):
            raise_error("SCENARIO.CHAPTER_ALREADY_EXISTS")
        outlines = get_existing_outlines(app, scenario_id)
        existing_chapters = [o for o in outlines if len(o.lesson_no) == 2]
        existing_chapter_count = len(existing_chapters)

        chapter_no = f"{existing_chapter_count + 1:02d}"

        if chapter_index == 0:
            chapter_index = existing_chapter_count + 1
        else:
            db.session.query(AILesson).filter(
                AILesson.course_id == scenario_id,
                AILesson.status.in_([STATUS_PUBLISH, STATUS_DRAFT]),
                AILesson.lesson_index >= chapter_index,
            ).update(
                {AILesson.lesson_index: AILesson.lesson_index + 1},
                synchronize_session=False,
            )
        chapter_id = generate_id(app)
        chapter = AILesson(
            lesson_id=chapter_id,
            lesson_no=chapter_no,
            lesson_name=chapter_name,
            lesson_desc=chapter_description,
            course_id=scenario_id,
            created_user_id=user_id,
            updated_user_id=user_id,
            status=STATUS_DRAFT,
            lesson_index=chapter_index,
            lesson_type=chapter_type,
        )
        check_text_with_risk_control(
            app, chapter_id, user_id, chapter.get_str_to_check()
        )
        db.session.add(chapter)
        db.session.commit()
        return ChapterDto(
            chapter.lesson_id,
            chapter.lesson_name,
            chapter.lesson_desc,
            chapter.lesson_type,
        )


# modify chapter
def modify_chapter(
    app,
    user_id: str,
    chapter_id: str,
    chapter_name: str,
    chapter_description: str,
    chapter_index: int = None,
    chapter_type: int = LESSON_TYPE_TRIAL,
):
    with app.app_context():
        chapter = AILesson.query.filter_by(lesson_id=chapter_id).first()
        if chapter:
            new_chapter = chapter.clone()
            new_chapter.lesson_name = chapter_name
            new_chapter.lesson_desc = chapter_description
            new_chapter.updated_user_id = user_id
            new_chapter.lesson_type = chapter_type
            new_chapter.status = STATUS_DRAFT
            new_chapter.lesson_index = chapter_index
            new_chapter.updated_at = datetime.now()
            if not new_chapter.equals(chapter):
                chapter.status = STATUS_HISTORY
                db.session.add(new_chapter)
            existing_chapter_count = AILesson.query.filter(
                AILesson.course_id == chapter.course_id,
                AILesson.status.in_([STATUS_PUBLISH, STATUS_DRAFT]),
                func.length(AILesson.lesson_no) == 2,
                AILesson.lesson_id != chapter_id,
                AILesson.lesson_name == chapter_name,
            ).count()
            if existing_chapter_count > 0:
                raise_error("SCENARIO.OTHER_SAME_CHAPTER_ALREADY_EXISTS")
            if chapter_index is not None:
                chapter.lesson_index = chapter_index
                db.session.query(AILesson).filter(
                    AILesson.course_id == chapter.course_id,
                    AILesson.status.in_([STATUS_PUBLISH, STATUS_DRAFT]),
                    AILesson.lesson_index >= chapter_index,
                    AILesson.lesson_id != chapter_id,
                ).update(
                    {AILesson.lesson_index: AILesson.lesson_index + 1},
                    synchronize_session=False,
                )
            old_check_str = chapter.get_str_to_check()
            new_check_str = new_chapter.get_str_to_check()
            if old_check_str != new_check_str:
                check_text_with_risk_control(app, chapter_id, user_id, new_check_str)
            db.session.commit()
            return ChapterDto(
                chapter.lesson_id,
                chapter.lesson_name,
                chapter.lesson_desc,
                chapter.lesson_type,
            )
        raise_error("SCENARIO.CHAPTER_NOT_FOUND")


# delete chapter
# @author: yfge
# @date: 2025-04-14
# delete chapter will also delete all the blocks under the chaper
# and change the lesson_no of the outlines under the chapter
def delete_chapter(app, user_id: str, chapter_id: str):
    with app.app_context():
        chapter = (
            AILesson.query.filter(
                AILesson.lesson_id == chapter_id,
                AILesson.status.in_([STATUS_PUBLISH, STATUS_DRAFT]),
            )
            .order_by(AILesson.id.desc())
            .first()
        )
        if chapter:
            if chapter.status == STATUS_PUBLISH:
                new_chapter = chapter.clone()
                new_chapter.status = STATUS_TO_DELETE
                new_chapter.updated_user_id = user_id
                new_chapter.updated_at = datetime.now()
                app.logger.info(
                    f"new_chapter: {new_chapter.lesson_id} {new_chapter.lesson_name} {new_chapter.status}"
                )
                db.session.add(new_chapter)
            else:
                chapter.status = STATUS_TO_DELETE
                chapter.updated_user_id = user_id
                chapter.updated_at = datetime.now()
            outlines = get_existing_outlines(app, chapter.course_id)
            for outline in outlines:
                if outline.lesson_no > chapter.lesson_no:
                    new_outline = outline.clone()
                    outline.status = STATUS_HISTORY
                    new_outline.status = STATUS_DRAFT
                    new_outline.updated_user_id = user_id
                    new_outline.updated_at = datetime.now()
                    new_chapter_index = int(outline.lesson_no[:2]) - 1
                    if len(new_outline.lesson_no) == 2:
                        new_outline.lesson_no = f"{new_chapter_index:02d}"
                    else:
                        new_outline.lesson_no = (
                            f"{new_chapter_index:02d}{new_outline.lesson_no[2:]}"
                        )
                    app.logger.info(
                        f"reorder outline: {outline.lesson_id} {outline.lesson_no} =>  {new_outline.lesson_no}"
                    )
                    db.session.add(new_outline)
            blocks = get_existing_blocks(app, [o.lesson_id for o in outlines])
            for block in blocks:
                if block.lesson_no > chapter.lesson_no:
                    block.status = STATUS_HISTORY
                    db.session.add(block)
            app.logger.info(f"outlines: {[o.lesson_no for o in outlines]}")
            db.session.commit()
            return True
        raise_error("SCENARIO.CHAPTER_NOT_FOUND")


# update chapter order
# @author: yfge
# @date: 2025-04-14
# update chapter order will also update the lesson_no of the outlines under the chapter
def update_chapter_order(
    app, user_id: str, scenario_id: str, chapter_ids: list
) -> list[ChapterDto]:
    with app.app_context():
        chapter_list = (
            AILesson.query.filter(
                AILesson.course_id == scenario_id,
                AILesson.lesson_id.in_(chapter_ids),
            )
            .order_by(AILesson.lesson_index.asc(), AILesson.lesson_no.asc())
            .all()
        )
        # check parent no
        parent_no = ""
        parent_id = None
        chapter_no_list = [len(chapter.lesson_no) for chapter in chapter_list]
        if len(set(chapter_no_list)) > 1:
            raise_error("SCENARIO.CHAPTER_NO_NOT_MATCH")

        if chapter_no_list[0] > 2:
            parent_no = chapter_list[0].lesson_no[:2]
            parent_id = chapter_list[0].parent_id
        else:
            parent_no = ""
            parent_id = ""
        for chapter in chapter_list:
            if len(chapter.lesson_no) > 2:
                if parent_no != "" and chapter.lesson_no[:2] != parent_no:
                    raise_error("SCENARIO.CHAPTER_PARENT_NO_NOT_MATCH")
                if parent_id is None:
                    parent_id = chapter.parent_id
                else:
                    if chapter.parent_id != parent_id:
                        raise_error("SCENARIO.CHAPTER_PARENT_ID_NOT_MATCH")
        chapter_dtos = []
        update_chatpers = []
        for index, chapter_id in enumerate(chapter_ids):
            chapter = next((c for c in chapter_list if c.lesson_id == chapter_id), None)
            if chapter:
                if chapter.lesson_index != index + 1:
                    chapter.lesson_index = index + 1
                    update_chatpers.append(chapter)
                    chapter.lesson_no = f"{parent_no}{index + 1:02d}"
                    chapter.updated_user_id = user_id
                    app.logger.info(
                        f"chapter.lesson_no: {chapter.lesson_no} {chapter.lesson_name}"
                    )
                    chapter.updated_at = datetime.now()
                chapter_dtos.append(
                    ChapterDto(
                        chapter.lesson_id,
                        chapter.lesson_name,
                        chapter.lesson_desc,
                        chapter.lesson_type,
                    )
                )
        if len(update_chatpers) > 0:
            sub_chapters = AILesson.query.filter(
                AILesson.course_id == scenario_id,
                AILesson.status.in_([STATUS_PUBLISH, STATUS_DRAFT]),
                AILesson.parent_id.in_([c.lesson_id for c in update_chatpers]),
            ).all()
            for sub_chapter in sub_chapters:
                parent = next(
                    (
                        c
                        for c in update_chatpers
                        if c.lesson_id == sub_chapter.parent_id
                    ),
                    None,
                )
                if parent:
                    app.logger.info(
                        f"update sub_chapter: {sub_chapter.lesson_id} {sub_chapter.lesson_name} {parent.lesson_id} {parent.lesson_name}"
                    )
                    sub_chapter.lesson_no = (
                        parent.lesson_no + f"{sub_chapter.lesson_index:02d}"
                    )
                    sub_chapter.parent_id = parent.lesson_id
                    sub_chapter.updated_user_id = user_id
                    sub_chapter.updated_at = datetime.now()
            db.session.commit()
        return chapter_dtos


# get outline tree
# @author: yfge
# @date: 2025-04-14
# get outline tree will return the outline tree of the scenario
# is used for the scenario outline page in the cook-web
def get_outline_tree(app, user_id: str, scenario_id: str):
    with app.app_context():
        outlines = get_existing_outlines(app, scenario_id)
        outline_tree_dto = [
            SimpleOutlineDto(node.lesson_id, node.lesson_no, node.lesson_name)
            for node in outlines
        ]
        need_to_update_parent = False
        for outline in outlines:
            if len(outline.lesson_no) > 2 and outline.parent_id == "":
                parent = next(
                    (c for c in outlines if c.lesson_no == outline.lesson_no[:-2]),
                    None,
                )
                if parent:
                    app.logger.info(
                        f"update outline parent_id: {outline.lesson_id} {outline.lesson_name} {parent.lesson_id} {parent.lesson_name}"
                    )
                    outline.parent_id = parent.lesson_id
                    need_to_update_parent = True
        if need_to_update_parent:
            db.session.commit()
        node_dict = {}
        outline_tree = []
        for node in outline_tree_dto:
            app.logger.info(f"node: {node.__json__()}")
            node_dict[node.outline_no] = node
        for node in outline_tree_dto:
            if len(node.outline_no) == 2:
                outline_tree.append(node_dict[node.outline_no])
            else:
                parent_no = node.outline_no[:-2]
                if parent_no in node_dict and parent_no != node.outline_no:
                    app.logger.info(
                        f"parent_no: {parent_no}, node.outline_no: {node.outline_no}"
                    )

                    node_dict[parent_no].outline_children.append(
                        node_dict[node.outline_no]
                    )
        return outline_tree
