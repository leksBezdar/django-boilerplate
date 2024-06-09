from ninja import Schema


class LoginInShema(Schema):
    phone: str


class LoginOutShema(Schema):
    message: str


class ConfirmInSchema(Schema):
    phone: str
    code: str


class ConfirmOutSchema(Schema):
    token: str
