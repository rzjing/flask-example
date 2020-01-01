# @Author   : Wang Xiaoqiang
# @GitHub   : https://github.com/rzjing
# @File     : __init__.py
# @Time     : 2020/1/1 22:27

from flask import Flask, jsonify

app = Flask(__name__)


def make_response(code=200, **kwargs):
    return jsonify(code=code, **kwargs)


if __name__ == '__main__':
    pass
