#!/usr/bin/env bash
sleep 3
python3 manage.py db upgrade
python3 run.py