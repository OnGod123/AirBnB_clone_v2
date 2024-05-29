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
    # Define the web_static folder path
    web_static_path = "web_static"
    
    # Define the versions folder path
    versions_path = "versions"

    # Create the versions directory if it doesn't exist
    if not os.path.exists(versions_path):
        os.makedirs(versions_path)

    # Generate the archive filename
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    archive_filename = f"web_static_{timestamp}.tgz"
    archive_path = os.path.join(versions_path, archive_filename)

    # Create the .tgz archive
    result = c.local(f"tar -czvf {archive_path} {web_static_path}")

    # Check if the archive was created successfully
    if result.ok:
        return archive_path
    else:
        return None

