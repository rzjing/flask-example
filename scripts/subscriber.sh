#!/usr/bin/env bash

cd /data/flask-example

[[ ! -e 'logs' ]] && mkdir logs

source scripts/env_dev.sh
source venv/bin/activate && pip install -r requirements.txt && python app/common/subscriber.py
