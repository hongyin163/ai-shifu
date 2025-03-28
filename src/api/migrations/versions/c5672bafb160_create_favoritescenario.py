"""create FavoriteScenario

Revision ID: c5672bafb160
Revises: ebd6acaf9989
Create Date: 2025-02-10 12:54:41.560002

"""

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = "c5672bafb160"
down_revision = "ebd6acaf9989"
branch_labels = None
depends_on = None


def upgrade():
    try:
        # ### commands auto generated by Alembic - please adjust! ###
        op.create_table(
            "scenario_favorite",
            sa.Column("id", mysql.BIGINT(), autoincrement=True, nullable=False),
            sa.Column(
                "scenario_id",
                sa.String(length=36),
                nullable=False,
                comment="Scenario UUID",
            ),
            sa.Column(
                "user_id", sa.String(length=36), nullable=False, comment="User UUID"
            ),
            sa.Column("status", sa.Integer(), nullable=False, comment="Status"),
            sa.Column(
                "created_at", sa.TIMESTAMP(), nullable=False, comment="Creation time"
            ),
            sa.Column(
                "updated_at", sa.TIMESTAMP(), nullable=False, comment="Update time"
            ),
            sa.PrimaryKeyConstraint("id"),
        )
        op.create_table(
            "select_question",
            sa.Column(
                "id",
                mysql.BIGINT(),
                autoincrement=True,
                nullable=False,
                comment="Unique ID",
            ),
            sa.Column(
                "question_id",
                sa.String(length=36),
                nullable=False,
                comment="Question ID",
            ),
            sa.Column(
                "script_id", sa.String(length=36), nullable=False, comment="Script ID"
            ),
            sa.Column(
                "logscript_id",
                sa.String(length=36),
                nullable=False,
                comment="Logscript ID",
            ),
            sa.Column(
                "user_id", sa.String(length=36), nullable=False, comment="User ID"
            ),
            sa.Column(
                "genration_model",
                sa.String(length=255),
                nullable=False,
                comment="Generation model",
            ),
            sa.Column(
                "genration_prompt",
                sa.Text(),
                nullable=False,
                comment="Generation prompt",
            ),
            sa.Column("question", sa.Text(), nullable=False, comment="Question"),
            sa.Column("options", sa.Text(), nullable=False, comment="Options"),
            sa.Column(
                "correct_answer",
                sa.String(length=255),
                nullable=False,
                comment="Correct answer",
            ),
            sa.Column(
                "created", sa.TIMESTAMP(), nullable=False, comment="Creation time"
            ),
            sa.Column("updated", sa.TIMESTAMP(), nullable=False, comment="Update time"),
            sa.Column(
                "status",
                sa.Integer(),
                nullable=False,
                comment="0 for deleted, 1 for active",
            ),
            sa.PrimaryKeyConstraint("id"),
        )
        with op.batch_alter_table("select_question", schema=None) as batch_op:
            batch_op.create_index(
                batch_op.f("ix_select_question_logscript_id"),
                ["logscript_id"],
                unique=False,
            )
            batch_op.create_index(
                batch_op.f("ix_select_question_question_id"),
                ["question_id"],
                unique=False,
            )
            batch_op.create_index(
                batch_op.f("ix_select_question_script_id"), ["script_id"], unique=False
            )
            batch_op.create_index(
                batch_op.f("ix_select_question_user_id"), ["user_id"], unique=False
            )
    except Exception:
        pass

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table("select_question", schema=None) as batch_op:
        batch_op.drop_index(batch_op.f("ix_select_question_user_id"))
        batch_op.drop_index(batch_op.f("ix_select_question_script_id"))
        batch_op.drop_index(batch_op.f("ix_select_question_question_id"))
        batch_op.drop_index(batch_op.f("ix_select_question_logscript_id"))

    op.drop_table("select_question")
    op.drop_table("scenario_favorite")
    # ### end Alembic commands ###
