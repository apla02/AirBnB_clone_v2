#!/usr/bin/python3.5
import os
from fabric.api import put, run, local, env
from datetime import datetime

env.hosts = ['34.75.211.58', '34.74.11.193']


def do_deploy(archive_path):
    '''distributes an archive to your web servers, using the function do_deploy
    '''
    # archive_path= "versions/web_static_20170315003959.tgz"
    path = archive_path.split('/')
    whole_file = path[1].split(".")
    filename = whole_file[0]
    if os.path.isfile("archive_path"):
        put("archive_path", "/tmp/")
        run("mkdir -p /data/web_static/releases/{}".format(filename))
        run("tar -xzf /tmp/{}.tgz -C /data/web_static/releases/{}/".format(
            filename, filename))
        run("rm /tmp/{}.tgz".format(filename))
        run("mv /data/web_static/releases/{}/web_static/*\
             /data/web_static/releases/{}/".format(filename, filename))
        run("rm -rf /data/web_static/releases/{}/web_static".format(filename))
        run("rm -rf /data/web_static/current")
        run("ln -s /data/web_static/releases/{}/\
             /data/web_static/current".format(filename))
        return True
    else:
        return False


def do_pack():
    '''
    script that generates a .tgz archive from the contents
    of the web_static folder of your AirBnB Clone repo,
    using the function do_pack
    '''
    try:
        now_string = datetime.now().strftime('%Y%m%d%H%M%S')
        filename = 'versions/web_static_' + now_string + '.tgz'
        print('Packing web_static to {}'.format(filename))
        local('mkdir -p versions')
        local('tar -cvzf {} web_static'.format(filename))
    except Exception:
        None
