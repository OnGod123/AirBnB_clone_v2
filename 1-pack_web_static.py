from fabric import task
from datetime import datetime
import os

@task
def do_pack(c):
    """
    Creates a .tgz archive from the contents of the web_static folder.

    Returns:
        Archive path if successful, None otherwise.
    """
    
    if not os.path.exists("versions"):
        os.makedirs("version")

    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    archive_path = "versions/web_static_{}.tgz".format(timestamp)

    
    result = c.local("tar -cvzf {} web_static".format(archive_path))

    
    if result.failed:
        return None
    else:
        return archive_path


