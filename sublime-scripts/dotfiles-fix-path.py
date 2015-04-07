import os

PATH = '/usr/local/nvm/current/bin'
CURRENT = os.environ['PATH']

os.environ['PATH'] = PATH + ':' + CURRENT
