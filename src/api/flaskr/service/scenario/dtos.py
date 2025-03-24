from flaskr.common.swagger import register_schema_to_swagger


@register_schema_to_swagger
class ScenarioDto:
    scenario_id: str
    scenario_name: str
    scenario_description: str
    scenario_image: str
    scenario_state: int
    is_favorite: bool

    def __init__(
        self,
        scenario_id: str,
        scenario_name: str,
        scenario_description: str,
        scenario_image: str,
        scenario_state: int,
        is_favorite: bool,
    ):
        self.scenario_id = scenario_id
        self.scenario_name = scenario_name
        self.scenario_description = scenario_description
        self.scenario_image = scenario_image
        self.scenario_state = scenario_state
        self.is_favorite = is_favorite

    def __json__(self):
        return {
            "id": self.scenario_id,
            "name": self.scenario_name,
            "description": self.scenario_description,
            "image": self.scenario_image,
            "state": self.scenario_state,
            "is_favorite": self.is_favorite,
        }


@register_schema_to_swagger
class ChapterDto:
    chapter_id: str
    chapter_name: str
    chapter_description: str
    chapter_type: int

    def __init__(
        self,
        chapter_id: str,
        chapter_name: str,
        chapter_description: str,
        chapter_type: int,
    ):
        self.chapter_id = chapter_id
        self.chapter_name = chapter_name
        self.chapter_description = chapter_description
        self.chapter_type = chapter_type

    def __json__(self):
        return {
            "chapter_id": self.chapter_id,
            "chapter_name": self.chapter_name,
            "chapter_description": self.chapter_description,
            "chapter_type": self.chapter_type,
        }


@register_schema_to_swagger
class SimpleOutlineDto:
    outline_id: str
    outline_no: str
    outline_name: str
    outline_children: list["SimpleOutlineDto"]

    def __init__(
        self,
        outline_id: str,
        outline_no: str,
        outline_name: str,
        outline_children: list["SimpleOutlineDto"] = None,
    ):
        self.outline_id = outline_id
        self.outline_no = outline_no
        self.outline_name = outline_name
        self.outline_children = outline_children if outline_children is not None else []

    def __json__(self):
        return {
            "id": self.outline_id,
            "no": self.outline_no,
            "name": self.outline_name,
            "children": self.outline_children,
        }


@register_schema_to_swagger
class UnitDto:
    unit_id: str
    unit_no: str
    unit_name: str


@register_schema_to_swagger
class OutlineDto:
    outline_id: str
    outline_no: str
    outline_name: str
    outline_desc: str
    outline_type: int

    def __init__(
        self,
        outline_id: str = None,
        outline_no: str = None,
        outline_name: str = None,
        outline_desc: str = None,
        outline_type: int = None,
    ):
        self.outline_id = outline_id
        self.outline_no = outline_no
        self.outline_name = outline_name
        self.outline_desc = outline_desc
        self.outline_type = outline_type

    def __json__(self):
        return {
            "id": self.outline_id,
            "no": self.outline_no,
            "name": self.outline_name,
            "desc": self.outline_desc,
            "type": self.outline_type,
        }


# prompt
@register_schema_to_swagger
class AIDto:
    prompt: str
    profiles: list[str]
    model: str
    temprature: float
    other_conf: dict

    def __init__(
        self,
        prompt: str = None,
        profiles: list[str] = None,
        model: str = None,
        temprature: float = None,
        other_conf: dict = None,
    ):
        self.prompt = prompt
        self.profiles = profiles
        self.model = model
        self.temprature = temprature
        self.other_conf = other_conf

    def __json__(self):
        return {
            "properties": {
                "prompt": self.prompt,
                "profiles": self.profiles,
                "model": self.model,
                "temprature": self.temprature,
                "other_conf": self.other_conf,
            },
            "type": __class__.__name__.replace("Dto", "").lower(),
        }


# prompt
@register_schema_to_swagger
class SystemPromptDto:
    prompt: str
    profiles: str
    model: str
    temprature: float
    other_conf: dict

    def __init__(
        self,
        prompt: str = None,
        profiles: list[str] = None,
        model: str = None,
        temprature: float = None,
        other_conf: dict = None,
    ):
        self.prompt = prompt
        self.profiles = profiles
        self.model = model
        self.temprature = temprature
        self.other_conf = other_conf

    def __json__(self):
        return {
            "properties": {
                "prompt": self.prompt,
                "profiles": self.profiles,
                "model": self.model,
                "temprature": self.temprature,
                "other_conf": self.other_conf,
            },
            "type": __class__.__name__.replace("Dto", "").lower(),
        }


@register_schema_to_swagger
class SolidContentDto:
    content: str

    def __init__(self, content: str = None, profiles: list[str] = None):
        self.content = content
        self.profiles = profiles

    def __json__(self):
        return {
            "properties": {
                "content": self.content,
                "profiles": self.profiles,
            },
            "type": __class__.__name__.replace("Dto", "").lower(),
        }


@register_schema_to_swagger
class ButtonDto:
    # type button
    button_name: str
    button_key: str

    def __init__(self, button_name: str = None, button_key: str = None):
        self.button_name = button_name
        self.button_key = button_key

    def __json__(self):
        return {
            "properties": {
                "button_name": self.button_name,
                "button_key": self.button_key,
            },
            "type": __class__.__name__.replace("Dto", "").lower(),
        }


@register_schema_to_swagger
class LoginDto(ButtonDto):
    # type login
    button_name: str
    button_key: str

    def __init__(self, button_name: str = None, button_key: str = None):
        super().__init__(button_name, button_key)
        self.button_name = button_name
        self.button_key = button_key

    def __json__(self):
        return {
            "properties": {
                "button_name": self.button_name,
                "button_key": self.button_key,
            },
            "type": __class__.__name__.replace("Dto", "").lower(),
        }


@register_schema_to_swagger
class GotoDtoItem:
    value: str
    type: str
    goto_id: str

    def __init__(self, value: str = None, type: str = None, goto_id: str = None):
        self.value = value
        self.type = type
        self.goto_id = goto_id

    def __json__(self):
        return {
            "value": self.value,
            "type": self.type,
            "goto_id": self.goto_id,
        }


@register_schema_to_swagger
class GotoSettings:
    items: list[GotoDtoItem]
    profile_key: str

    def __init__(
        self, items: list[GotoDtoItem] = None, profile_key: str = None, **kwargs
    ):
        if isinstance(items, list):
            self.items = [
                GotoDtoItem(**item) if isinstance(item, dict) else item
                for item in items
            ]
        self.profile_key = profile_key

    def __json__(self):
        return {
            "items": self.items,
            "profile_key": self.profile_key,
        }


@register_schema_to_swagger
class GotoDto(ButtonDto):
    # type goto
    button_name: str
    button_key: str
    goto_settings: GotoSettings

    def __init__(
        self,
        button_name: str = None,
        button_key: str = None,
        goto_settings: GotoSettings = None,
        **kwargs
    ):
        super().__init__(button_name, button_key)
        if isinstance(goto_settings, dict):
            self.goto_settings = GotoSettings(**goto_settings)
        else:
            self.goto_settings = goto_settings
        button_key

    def __json__(self):
        return {
            "properties": {
                "goto_settings": self.goto_settings,
                "button_name": self.button_name,
                "button_key": self.button_key,
            },
            "type": __class__.__name__.replace("Dto", "").lower(),
        }


@register_schema_to_swagger
class PaymentDto(ButtonDto):
    # type payment
    button_name: str
    button_key: str

    def __init__(self, button_name: str = None, button_key: str = None):
        super().__init__(button_name, button_key)
        self.button_name = button_name
        self.button_key = button_key

    def __json__(self):
        return {
            "properties": {
                "button_name": self.button_name,
                "button_key": self.button_key,
            },
            "type": __class__.__name__.replace("Dto", "").lower(),
        }


@register_schema_to_swagger
class ContinueDto(ButtonDto):
    # type continue
    button_name: str
    button_key: str

    def __init__(self, button_name: str = None, button_key: str = None):
        super().__init__(button_name, button_key)


@register_schema_to_swagger
class OptionDto:
    # type option
    option_name: str
    option_key: str
    profile_key: str
    buttons: list[ButtonDto]

    def __init__(
        self,
        option_name: str = None,
        option_key: str = None,
        profile_key: str = None,
        buttons: list = None,
    ):
        self.option_name = option_name
        self.option_key = option_key
        self.profile_key = profile_key
        if isinstance(buttons, list):
            self.buttons = [
                ButtonDto(**button) if isinstance(button, dict) else button
                for button in buttons
            ]

    def __json__(self):
        return {
            "properties": {
                "option_name": self.option_name,
                "option_key": self.option_key,
                "profile_key": self.profile_key,
                "buttons": self.buttons,
            },
            "type": __class__.__name__.replace("Dto", "").lower(),
        }


@register_schema_to_swagger
class InputDto:
    # type text input
    input_name: str
    input_key: str
    input_placeholder: str

    def __init__(
        self,
        text_input_name: str = None,
        text_input_key: str = None,
        text_input_placeholder: str = None,
    ):
        self.text_input_name = text_input_name
        self.text_input_key = text_input_key
        self.text_input_placeholder = text_input_placeholder

    def __json__(self):
        return {
            "properties": {
                "text_input_name": self.text_input_name,
                "text_input_key": self.text_input_key,
                "text_input_placeholder": self.text_input_placeholder,
            },
            "type": __class__.__name__.replace("Dto", "").lower(),
        }


@register_schema_to_swagger
class TextInputDto(InputDto):
    # type text input
    prompt: AIDto
    input_name: str
    input_key: str
    input_placeholder: str

    def __init__(
        self,
        text_input_name: str = None,
        text_input_key: str = None,
        text_input_placeholder: str = None,
        prompt: AIDto = None,
    ):
        super().__init__(text_input_name, text_input_key, text_input_placeholder)
        self.prompt = prompt
        self.input_name = text_input_name
        self.input_key = text_input_key
        self.input_placeholder = text_input_placeholder
        if isinstance(prompt, dict):
            self.prompt = AIDto(**prompt)
        elif isinstance(prompt, AIDto):
            self.prompt = prompt

    def __json__(self):
        return {
            "properties": {
                "prompt": self.prompt,
                "input_name": self.input_name,
                "input_key": self.input_key,
                "input_placeholder": self.input_placeholder,
            },
            "type": __class__.__name__.replace("Dto", "").lower(),
        }


@register_schema_to_swagger
class CodeDto(InputDto):
    # type code
    input_name: str
    input_key: str
    input_placeholder: str

    def __init__(
        self,
        text_input_name: str = None,
        text_input_key: str = None,
        text_input_placeholder: str = None,
    ):
        super().__init__(text_input_name, text_input_key, text_input_placeholder)
        self.input_name = text_input_name
        self.input_key = text_input_key
        self.input_placeholder = text_input_placeholder

    def __json__(self):
        return {
            "properties": {
                "input_name": self.input_name,
                "input_key": self.input_key,
                "input_placeholder": self.input_placeholder,
            },
            "type": __class__.__name__.replace("Dto", "").lower(),
        }


@register_schema_to_swagger
class PhoneDto(InputDto):
    # type phone
    input_name: str
    text_input_key: str
    text_input_placeholder: str

    def __init__(
        self,
        text_input_name: str = None,
        text_input_key: str = None,
        text_input_placeholder: str = None,
    ):
        super().__init__(text_input_name, text_input_key, text_input_placeholder)
        self.input_name = text_input_name
        self.input_key = text_input_key
        self.input_placeholder = text_input_placeholder

    def __json__(self):
        return {
            "properties": {
                "input_name": self.input_name,
                "input_key": self.input_key,
                "input_placeholder": self.input_placeholder,
            },
            "type": __class__.__name__.replace("Dto", "").lower(),
        }


@register_schema_to_swagger
class BlockDto:
    block_id: str
    block_no: str
    block_name: str
    block_desc: str
    block_type: int
    block_index: int
    block_content: AIDto | SolidContentDto
    block_ui: OptionDto | TextInputDto | ButtonDto

    def __init__(
        self,
        block_id: str = None,
        block_no: str = None,
        block_name: str = None,
        block_desc: str = None,
        block_type: int = None,
        block_index: int = None,
        block_content: AIDto | SolidContentDto | SystemPromptDto = None,
        block_ui: OptionDto | TextInputDto | ButtonDto = None,
        **kwargs
    ):
        self.block_id = block_id
        self.block_no = block_no
        self.block_name = block_name
        self.block_desc = block_desc
        self.block_type = block_type
        self.block_index = block_index
        self.block_content = block_content
        self.block_ui = block_ui

    def __json__(self):
        return {
            "properties": {
                "block_id": self.block_id,
                "block_no": self.block_no,
                "block_name": self.block_name,
                "block_desc": self.block_desc,
                "block_type": self.block_type,
                "block_index": self.block_index,
                "block_content": self.block_content,
                "block_ui": self.block_ui,
            },
            "type": __class__.__name__.replace("Dto", "").lower(),
        }


@register_schema_to_swagger
class OutlineEditDto:
    outline_id: str
    outline_no: str
    outline_name: str
    outline_desc: str
    outline_type: int
    outline_level: int

    def __init__(
        self,
        outline_id: str = None,
        outline_no: str = None,
        outline_name: str = None,
        outline_desc: str = None,
        outline_type: int = None,
    ):
        self.outline_id = outline_id
        self.outline_no = outline_no
        self.outline_name = outline_name
        self.outline_desc = outline_desc
        self.outline_type = outline_type
        self.outline_level = len(outline_no) // 2

    def __json__(self):
        return {
            "properties": {
                "outline_id": self.outline_id,
                "outline_no": self.outline_no,
                "outline_name": self.outline_name,
                "outline_desc": self.outline_desc,
                "outline_type": self.outline_type,
                "outline_level": self.outline_level,
            },
            "type": "outline",
        }
