#!/usr/bin/env bash

cd /data/flask-example

source venv/bin/activate && pip install -r requirements.txt && python app/common/subscriber.py
