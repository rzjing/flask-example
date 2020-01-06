# @Author   : Wang Xiaoqiang
# @GitHub   : https://github.com/rzjing
# @Time     : 2020-01-06 15:59
# @File     : gun.py

# gunicorn configuration file

# import multiprocessing

bind = '0.0.0.0:5000'
# workers = multiprocessing.cpu_count() * 2 + 1

loglevel = 'info'
access_log_format = '%(h)s %(l)s %(u)s %(t)s "%(r)s" %(s)s %(b)s "%(f)s" "%(a)s" %(L)s'

reload = True

if __name__ == '__main__':
    pass
