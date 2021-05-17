#!/bin/bash

# For windows
# this launch script lauch in a single command the server but not the container

#da ripensare assolutamente
python -m venv ENV && source ENV/Scripts/activate && pip install -r requirements-lock.txt && export FLASK_APP=web.py && export FLASK_DEBUG=1 && flask run --host=0.0.0.0 --port=5001
