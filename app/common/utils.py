# @Author   : Wang Xiaoqiang
# @GitHub   : https://github.com/rzjing
# @File     : utils.py
# @Time     : 2020/1/2 23:19

import os


def say(word):
    print(f'PPID: {os.getppid()} PID: {os.getpid()} Say -> hello {word}')


if __name__ == '__main__':
    pass
