# @Author   : Wang Xiaoqiang
# @GitHub   : https://github.com/rzjing
# @File     : subscriber.py
# @Time     : 2020/1/5 21:07

import logging

from app.config import Config
from app.model import Redis

logging.basicConfig(format='%(asctime)s %(levelname)s %(message)s', datefmt='%Y-%m-%d %H:%M:%S', level=logging.INFO)


class Subscriber(object):

    def __init__(self):
        self.conf = Config()
        self.redis = Redis(**self.conf.get_redis())

    def start(self, channel: str):
        self.redis.subscribe(channel, self.callback)

    @staticmethod
    def callback(response: dict):
        if response['type'] == 'subscribe':
            logging.info(f'Subscriber is running...\n')
        elif response['type'] == 'message':
            channel, message = response['channel'].decode('utf8'), response['data'].decode('utf8')
            logging.info(f'Response -> channel: {channel} message: {message}')


if __name__ == '__main__':
    Subscriber().start('test:public')
