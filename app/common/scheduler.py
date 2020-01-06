# @Author   : Wang Xiaoqiang
# @GitHub   : https://github.com/rzjing
# @File     : scheduler.py
# @Time     : 2020/1/5 15:34

from apscheduler.jobstores.redis import RedisJobStore
from apscheduler.schedulers.background import BackgroundScheduler

from app.config import Config


class Scheduler(object):

    def __init__(self):
        self.conf = Config()
        self.scheduler = BackgroundScheduler(jobstores={'redis': RedisJobStore(**self.conf.get_redis())})

    def add_job(self, func, trigger: str, params=None, next_run_time=None, jobstore='default', **trigger_args):
        """
        :param func: 执行函数
        :param trigger: 任务类型, Options: ['once', 'interval', 'cron']
        :param params: 执行函数参数列表
        :param next_run_time: 任务执行时间, 当 trigger='once' 时, 必传 next_run_time: datetime.datetime
        :param jobstore: 任务存储器, Options: ['default', 'redis']
        :param trigger_args: e.g. if trigger == 'interval': Options: ['days', 'hours', 'minutes', 'seconds', ...]
                                  elif trigger == 'cron': Options: ['year', 'month', 'day', 'week', 'day_of_week', ...]
        :return: Job
        """
        if trigger == 'once':
            job = self.scheduler.add_job(func, next_run_time=next_run_time, args=params, jobstore=jobstore)
        else:
            job = self.scheduler.add_job(func, trigger, args=params, **trigger_args, jobstore=jobstore)
        return job

    def get_job(self, job_id: str):
        """
        :param job_id: 任务ID
        :return: Job
        """
        return self.scheduler.get_job(job_id)

    def get_jobs(self):
        """
        :return: list[Job]
        """
        return self.scheduler.get_jobs()

    def del_job(self, job_id: str):
        """
        :param job_id: 任务ID
        """
        self.scheduler.remove_job(job_id)

    def del_jobs(self):
        self.scheduler.remove_all_jobs()

    def start(self):
        self.scheduler.start()


if __name__ == '__main__':
    pass
