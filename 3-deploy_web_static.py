from fabric import task, Connection
import os


web_servers = ['<IP web-01>', '<IP web-02>']

@task(hosts=web_servers)
def deploy(c):
    """
    Creates and distributes an archive to web servers.

    Returns:
        True if deployment is successful, otherwise False.
    """

    archive_path = do_pack()

    
    if not archive_path:
        print("No archive created. Deployment aborted.")
        return False

    
    result = do_deploy(archive_path)


    return result


def do_pack():
    """
    Creates a .tgz archive from the contents of the web_static folder.

    Returns:
        Archive path if successful, None otherwise.
    """
    try:
        
        web_static_path = "web_static"
        
        
        versions_path = "versions"

        
        if not os.path.exists(versions_path):
            os.makedirs(versions_path)

        
        timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
        archive_filename = f"web_static_{timestamp}.tgz"
        archive_path = os.path.join(versions_path, archive_filename)

        
        result = local(f"tar -czvf {archive_path} {web_static_path}")

        
        if result.failed:
            return None
        else:
            return archive_path
    except Exception as e:
        print(f"An error occurred while creating the archive: {e}")
        return None


def do_deploy(archive_path):
    """
    Distributes the archive to web servers and deploys it.

    Args:
        archive_path: Path to the archive to deploy.

    Returns:
        True if deployment is successful, otherwise False.
    """
    try:
        # Put your deployment logic here
        # Example:
        # run('ls -l')
        # run('uname -a')
        return True
    except Exception as e:
        print(f"An error occurred during deployment: {e}")
        return False

