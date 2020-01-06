# @Author   : Wang Xiaoqiang
# @GitHub   : https://github.com/rzjing
# @Time     : 2020-01-06 11:05
# @File     : subscriber.py

from flask_restful import Resource

from app import v1, redis, make_response, parser

_parser = parser.copy()
_parser.add_argument('channel', type=str, default='test:public', location='form', required=True, help='publish channel')
_parser.add_argument('message', type=str, location='form', required=True, help='publish message')


class Subscriber(Resource):

    def __init__(self):
        self.error = None
        self.args = _parser.parse_args()

    def post(self):
        redis.publish(self.args['channel'], self.args['message'])
        return make_response(info='ok')


v1.add_resource(Subscriber, '/subscriber')

if __name__ == '__main__':
    pass
