from flask import Flask
import config
from extensions import db
from models import UserModel
from blueprints.qa import bp as qa_bp
from blueprints.user import bp as user_bp

app = Flask(__name__)
# 导入config设置模块
app.config.from_object(config)
# 先创建，再绑定插件，避免在创建时候同时进行绑定
db.init_app(app)
# 写入blueprint进行模块化增强可读性
app.register_blueprint(qa_bp)
app.register_blueprint(user_bp)

@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'


if __name__ == '__main__':
    app.run()
