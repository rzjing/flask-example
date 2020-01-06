# @Author   : Wang Xiaoqiang
# @GitHub   : https://github.com/rzjing
# @File     : scheduler.py
# @Time     : 2020/1/2 23:01

from datetime import datetime

from apscheduler.jobstores.base import JobLookupError
from flask_restful import Resource

from app import v1, scheduler, make_response, parser
from app.common.utils import say

_parser = parser.copy()
_parser.add_argument('id', type=str, location='args', help='job.id')
_parser.add_argument('trigger', type=str, default='once', choices=['once', 'interval', 'cron'], location='form')
_parser.add_argument('jobstore', type=str, default='default', choices=['default', 'redis'], location=['args', 'form'])


class Scheduler(Resource):

    def __init__(self):
        self.error = None
        self.args = _parser.parse_args()

    def get(self):
        if self.args['id']:
            job = scheduler.get_job(self.args['id'])
            return make_response(job={'id': job.id, 'next_run_time': job.next_run_time, 'args': job.args})
        else:
            jobs = scheduler.get_jobs()
            return make_response(
                jobs=[{'id': job.id, 'next_run_time': job.next_run_time, 'args': job.args} for job in jobs]
            )

    def post(self):
        trigger, jobstore = self.args['trigger'], self.args['jobstore']
        if trigger == 'once':
            job = scheduler.add_job(say, 'once', next_run_time=datetime.now(), params=[f'{trigger} -> add_job'])
        elif trigger == 'interval':
            job = scheduler.add_job(say, 'interval', seconds=3, params=[f'{trigger} -> add_job'], jobstore=jobstore)
        else:
            job = scheduler.add_job(say, 'cron', minute='*/2', params=[f'{trigger} -> add_job'], jobstore=jobstore)
        return make_response(job={'id': job.id, 'next_run_time': job.next_run_time, 'args': job.args})

    def delete(self):
        try:
            if self.args['id']:
                scheduler.del_job(self.args['id'])
            else:
                scheduler.del_jobs()
        except JobLookupError as e:
            return make_response(code=400, error=e.args[0])
        return make_response(info='deleted')


v1.add_resource(Scheduler, '/scheduler')

if __name__ == '__main__':
    pass
