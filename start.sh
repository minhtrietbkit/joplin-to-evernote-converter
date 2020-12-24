#!/bin/bash

source env/bin/activate

python manage.py runserver

# Run functional test
# python functional_tests.py
# Run unit test
# python manage.py test