#!/bin/bash

BASEDIR=$(dirname "$0")
$BASEDIR/venv/bin/python3 manage.py runserver --settings=retrato.config.local_settings 0.0.0.0:8080
