from fabric import task, Connection
import os


web_servers = ['<IP web-01>', '<IP web-02>']

@task(hosts=web_servers)
def do_deploy(c, archive_path):
    """
    Distributes an archive to web servers.

    Args:
        archive_path: Path to the archive to deploy.

    Returns:
        True if all operations are done correctly, otherwise False.
    """
    try:
    
        if not c.local(f'test -e {archive_path}', hide=True).ok:
            print(f"Archive file '{archive_path}' doesn't exist.")
            return False

        
        remote_tmp_dir = '/tmp/'
        remote_releases_dir = '/data/web_static/releases/'
        remote_current_dir = '/data/web_static/current'

        
        c.put(archive_path, remote=remote_tmp_dir)

        
        archive_filename = os.path.basename(archive_path)
        archive_name_without_ext = os.path.splitext(archive_filename)[0]

        
        with c.cd(remote_releases_dir):
            c.run(f'mkdir -p {archive_name_without_ext}')
            c.run(f'tar -xzf {remote_tmp_dir}{archive_filename} -C {archive_name_without_ext}')

        
        c.run(f'rm {remote_tmp_dir}{archive_filename}')

    
        c.run(f'rm -f {remote_current_dir}')

        
        c.run(f'ln -s {remote_releases_dir}{archive_name_without_ext} {remote_current_dir}')

        print("Deployment successful.")
        return True

    except Exception as e:
        print(f"An error occurred: {e}")
        return False

