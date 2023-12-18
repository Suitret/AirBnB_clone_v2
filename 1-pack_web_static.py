#!/usr/bin/python3
"""Fabric script (based on the file 1-pack_web_static.py) that distributes
an archive to your web servers, using the function do_deploy
"""
from fabric.api import local
from datetime import datetime


def do_pack():
    """
    Create a compressed archive of the web_static folder.
    Returns:
        Path to the archive if successful, None otherwise.
    """
    try:
        # Get the current timestamp for the archive name
        now = datetime.now()
        timestamp = now.strftime("%Y%m%d%H%M%S")

        # Create the versions directory if it doesn't exist
        local("mkdir -p versions")

        # Archive the web_static folder
        archive_name = "versions/web_static_{}.tgz".format(timestamp)
        local("tar -cvzf {} web_static".format(archive_name))

        return archive_name
    except Exception as e:
        return None
