#!/usr/bin/python3
'# generates a .tgz archive from the contents of the web static'

from datetime import datetime
from fabric.api import local


def do_pack():
    '# compress file'
    try:
        date = datetime.utcnow().strftime('%Y%m%d%H%M%S')
        local("sudo mkdir -p versions")
        local("sudo tar -cvzf versions/web_static_{}.tgz web_static".format(date))
        return "versions/web_static_{}.tgz web_static".format(date)
    except Exception:
        return None
