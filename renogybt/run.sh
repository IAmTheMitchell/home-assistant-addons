#!/usr/bin/with-contenv bashio

ls /

echo "ls /data"

ls /data

echo "ls /app"

ls /app

. /app/venv/bin/activate

python3 renogybtaddon.py
