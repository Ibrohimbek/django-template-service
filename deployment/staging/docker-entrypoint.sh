#!/bin/sh

echo "Starting server"
gunicorn --reload -b 0.0.0.0:8051 loadboard.wsgi --workers 5 --timeout 300 --log-level warning --log-file /opt/gunicorn.log
