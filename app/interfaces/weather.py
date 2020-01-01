# @Author   : Wang Xiaoqiang
# @GitHub   : https://github.com/rzjing
# @File     : weather.py
# @Time     : 2020/1/1 23:00

import json

import requests
from flask_restful import Resource

from app import v1, make_response


class Weather(Resource):

    def __init__(self):
        self.error = None
        # 中国天气网 北京天气信息
        self.weather = 'http://www.weather.com.cn/data/sk/101010100.html'

    def get(self):
        r = requests.get(self.weather)
        if r.status_code == 200:
            result: dict = json.loads(r.text.encode(r.encoding).decode('utf8'))
            return make_response(**result)
        else:
            self.error = r.reason
        return make_response(code=400, error=self.error)


v1.add_resource(Weather, '/weather')

if __name__ == '__main__':
    pass
