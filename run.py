# @Author   : Wang Xiaoqiang
# @GitHub   : https://github.com/rzjing
# @File     : run.py
# @Time     : 2020/1/1 22:27

from app import app, make_response


@app.route('/')
def trying():
    return make_response(info='hello world')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5010, debug=True)
