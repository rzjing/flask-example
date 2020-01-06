#!/usr/bin/env bash

export RUN_MODE=gunicorn

[[ ! -e 'logs' ]] && mkdir logs

source scripts/env_dev.sh
source venv/bin/activate && pip install -r requirements.txt

gunicorn -c gun.py -p gun.pid --access-logfile logs/access.log --error-logfile logs/error.log run:app -D
