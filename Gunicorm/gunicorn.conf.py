command='/home/tom/cli/bin/gunicorn'
pythonpath = '/home/tom/demoproject'
bind = '192.168.1.12:8089'
workers =3
accesslog = "access.log"
errorlog = "error.log"
access_log_format = '"%(r)s %(h)s %(l)s %(t)s %(s)s '
