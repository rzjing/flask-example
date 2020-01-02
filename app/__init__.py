# @Author   : Wang Xiaoqiang
# @GitHub   : https://github.com/rzjing
# @File     : __init__.py
# @Time     : 2020/1/1 22:27

from flask import Flask, jsonify
from flask_restful import Api

from .config import Config
from .model import MySQL, Redis

app = Flask(__name__)
v1 = Api(app, prefix='/v1')

conf = Config()

mysql = MySQL(**conf.get_mysql())
redis = Redis(**conf.get_redis())


def make_response(code=200, **kwargs):
    return jsonify(code=code, **kwargs)


if __name__ == '__main__':
    pass
