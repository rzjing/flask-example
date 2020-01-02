# @Author   : Wang Xiaoqiang
# @GitHub   : https://github.com/rzjing
# @File     : scheduler.py
# @Time     : 2020/1/2 23:01

from flask_restful import Resource
from apscheduler.jobstores.base import JobLookupError

from app import v1, scheduler, make_response, parser
from app.common.utils import say

_parser = parser.copy()
_parser.add_argument('id', type=str, location='args', help='job.id')


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

    @staticmethod
    def post():
        job = scheduler.add_job(say, 'interval', seconds=3, args=['add_job'])
        return make_response(job={'id': job.id, 'next_run_time': job.next_run_time, 'args': job.args})

    def delete(self):
        try:
            if self.args['id']:
                scheduler.remove_job(self.args['id'])
            else:
                scheduler.remove_all_jobs()
        except JobLookupError as e:
            return make_response(code=400, error=e.args[0])
        return make_response(info='deleted')


v1.add_resource(Scheduler, '/scheduler')

if __name__ == '__main__':
    pass
