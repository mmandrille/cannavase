#!/bin/bash
cd /opt/cannavase
source venv/bin/activate
cd /opt/cannavase/cannavase
gunicorn cannavase.wsgi -t 600 -b 127.0.0.1:8000 -w 6 --user=servidor --group=servidor --log-file=/opt/cier2019/gunicorn.log 2>>/opt/cier2019/gunicorn.log
