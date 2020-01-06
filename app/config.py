# @Author   : Wang Xiaoqiang
# @GitHub   : https://github.com/rzjing
# @Time     : 2020-01-02 16:14
# @File     : config.py

import os


class Config(object):

    def __init__(self):
        self.env = os.getenv('ENV', 'local')
        self.conf_mysql = {
            'dev': {
                'host': '192.168.10.22', 'port': 3306,
                'user': 'example', 'password': '123456', 'database': 'flask_example'
            },
            'local': {
                'host': '127.0.0.1', 'port': 3306,
                'user': 'example', 'password': '123456', 'database': 'flask_example'
            }
        }
        self.conf_redis = {
            'dev': {
                'host': '192.168.10.22', 'port': 6379, 'password': '123456', 'db': 0
            },
            'local': {
                'host': '127.0.0.1', 'port': 6379, 'password': '123456', 'db': 0
            }
        }

    def get_mysql(self):
        return self.conf_mysql[self.env]

    def get_redis(self):
        return self.conf_redis[self.env]


if __name__ == '__main__':
    pass
