# @Author   : Wang Xiaoqiang
# @GitHub   : https://github.com/rzjing
# @Time     : 2020-01-02 16:20
# @File     : model.py

import logging

import pymysql
import redis
from pymysql.err import OperationalError, IntegrityError, InternalError, ProgrammingError


class MySQL(object):

    def __init__(self, **kwargs):
        self.params = kwargs
        self.params.update({'charset': 'utf8mb4', 'cursorclass': pymysql.cursors.DictCursor})
        try:
            self.connection = pymysql.connect(**self.params)
        except OperationalError as e:
            logging.error(e)

    @property
    def get_params(self):
        return self.params

    def execute(self, sql: str, many=False, long=False):
        """
        :param sql: sql
        :param many: True 返回多值, False 返回单值
        :param long: True 长链接, 需要显示调用 self.commit(), self.close(); False 短链接, 一次调用关闭链接
        :return: cursor.fetchone() or cursor.fetchall()
        """
        try:
            self.connection.connect()
            with self.connection.cursor() as cursor:
                try:
                    cursor.execute(sql)
                except (IntegrityError, InternalError, ProgrammingError) as e:
                    logging.error(sql)
                    logging.error(e)
                else:
                    if many:
                        return cursor.fetchall()
                    else:
                        return cursor.fetchone()
        except OperationalError as e:
            logging.error(e)
        finally:
            if not long:
                self.commit()
                self.close()

    def executemany(self, sql: str, data: list, many=False, long=False):
        """
        :param sql: sql
        :param data: list[tuple(), tuple()]
        :param many: True 返回多值, False 返回单值
        :param long: True 长链接, 需要显示调用 self.commit(), self.close(); False 短链接, 一次调用关闭链接
        :return: cursor.fetchone() or cursor.fetchall()
        """
        try:
            self.connection.connect()
            with self.connection.cursor() as cursor:
                try:
                    cursor.executemany(sql, data)
                except (IntegrityError, InternalError, ProgrammingError) as e:
                    logging.error(sql)
                    logging.error(e)
                else:
                    if many:
                        return cursor.fetchall()
                    else:
                        return cursor.fetchone()

        except OperationalError as e:
            logging.error(e)

        finally:
            if not long:
                self.commit()
                self.close()

    def commit(self):
        self.connection.commit()

    def close(self):
        self.connection.close()


class Redis(object):

    def __init__(self, **kwargs):
        self.params = kwargs
        self.pool = redis.ConnectionPool(**self.params)
        self.connection = redis.Redis(connection_pool=self.pool)

    def set(self, key, val):
        self.connection.sadd(key, val)

    def get(self, key):
        return self.connection.smembers(key)

    def rem(self, key, val):
        return self.connection.srem(key, val)

    def delete(self, key):
        self.connection.delete(key)

    def publish(self, channel: str, message: str):
        self.connection.publish(channel, message)

    def subscribe(self, channel):
        sub = self.connection.pubsub()
        sub.subscribe(channel)
        return sub


if __name__ == '__main__':
    pass
