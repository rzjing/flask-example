#!/usr/bin/env bash

cd /data/flask-example

source env/dev.sh
source venv/bin/activate && pip install -r requirements.txt && python app/common/subscriber.py
