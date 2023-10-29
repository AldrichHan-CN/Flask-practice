# 这个文件是第三方的插件导入，防止循环引用（**1需要2执行，2需要1执行）
# 导入数据库连接插件
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
