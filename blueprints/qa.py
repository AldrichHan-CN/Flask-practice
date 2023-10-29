from flask import blueprints

bp = blueprints("qa", __name__, url_prefix="/")
# 把这个组件定义到根路径‘/’，作为首页
@bp.route("/")
def index():
    pass