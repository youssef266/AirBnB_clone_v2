#!/usr/bin/python3
"""This module defines a class to manage database storage for hbnb clone
"""
from fabric.api import local
from datetime import datetime

def do_pack():
    """Generates a .tgz archive from the contents of
    the web_static folder"""
    try:
        current_time = datetime.now().strftime("%Y%m%d%H%M%S")
        archive_name = "web_static_" + current_time + ".tgz"
        local("mkdir -p versions")
        local("tar -czvf versions/{} web_static".format(archive_name))
        return "versions/{}".format(archive_name)
    except:
        return None
