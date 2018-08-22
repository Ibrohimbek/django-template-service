#!/bin/sh

# Start server
echo "Starting Loadboard backend server"
python3 manage.py runserver 0.0.0.0:8051
