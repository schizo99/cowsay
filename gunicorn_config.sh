#!/bin/ash
gunicorn -c config.py app:app -b 0.0.0.0:8080