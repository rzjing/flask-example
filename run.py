# @Author   : Wang Xiaoqiang
# @GitHub   : https://github.com/rzjing
# @File     : run.py
# @Time     : 2020/1/1 22:27

import os

from app import app, scheduler, make_response, interfaces


@app.route('/')
def trying():
    return make_response(info='hello world')


if __name__ == '__main__':
    # 调试模式下解决代码重载导致自动加载的计划任务在多个线程中同时执行的问题
    if os.getenv('WERKZEUG_RUN_MAIN') == 'true':
        scheduler.start()
    app.run(host='0.0.0.0', port=os.getenv('SERVER_PORT', 5000), debug=True)
