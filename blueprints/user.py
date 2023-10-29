# 一旦引入了blueprints，这个东西就成为了flask的子文件
from flask import Blueprint

# 用blueprint创建对象,适度函数，以后的所有和此相关的url都需要有'/user' 前缀
bp = Blueprint("auth", __name__, url_prefix="/user")

@bp.route("login")
def login():
        pass