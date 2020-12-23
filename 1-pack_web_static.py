#!/usr/bin/python
from fabric.api import local
from datetime import datetime

def do_pack():
    try:
        now_string = datetime.now().strftime('%Y%m%d%H%M%S')
        filename= 'versions/web_static_'+ now_string + '.tgz'
        local('mkdir -p versions')
        local('tar -cvzf {} web_static'.format(filename))
        print('Packing web_static to versions/{}'.format(filename))
    except:
        None
