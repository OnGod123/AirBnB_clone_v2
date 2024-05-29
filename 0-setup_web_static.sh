#!/bin/bash
# Script to set up web servers for the deployment of web_static

# Update package list and install Nginx if it's not already installed
if ! which nginx > /dev/null; then
    sudo apt-get update
    sudo apt-get -y install nginx
fi

# Create the necessary directories
sudo mkdir -p /data/web_static/releases/test/
sudo mkdir -p /data/web_static/shared/

# Create a fake HTML file with simple content
echo "<html>
  <head>
  </head>
  <body>
    Welcome to web_static test!
  </body>
</html>" | sudo tee /data/web_static/releases/test/index.html

# Create a symbolic link, recreate it if it already exists
if [ -L /data/web_static/current ]; then
    sudo rm /data/web_static/current
fi
sudo ln -s /data/web_static/releases/test/ /data/web_static/current

# Give ownership of the /data/ folder to the ubuntu user and group
sudo chown -R ubuntu:ubuntu /data/

# Update the Nginx configuration
sudo sed -i '/server_name _;/a \\n\tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t}\n' /etc/nginx/sites-available/default

# Restart Nginx to apply the changes
sudo service nginx restart

# Exit successfully
exit 0

