#!/usr/bin/env bash

cd /data/flask-example

source scripts/env_dev.sh
source venv/bin/activate && pip install -r requirements.txt && python app/common/subscriber.py
