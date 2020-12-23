#!/usr/bin/env bash
# sets up your web servers for the deployment of web_static
sudo apt-get update
sudo apt-get -y install nginx
sudo mkdir -p /data/
sudo mkdir -p /data/web_static/
sudo mkdir -p /data/web_static/releases/
sudo mkdir -p /data/web_static/shared/
sudo mkdir -p /data/web_static/releases/test/
sudo echo 'hello' | sudo tee /data/web_static/releases/test/index.html
sudo ln -sf /data/web_static/current /data/web_static/releases/test/
sudo chown  -R ubuntu:ubuntu /data/
sudo sed -i '43 a\\tlocation \/hbnb_static\/ {\n\talias \/data\/web_static\/current\/;\n\t}\n ' /etc/nginx/sites-available/default
sudo service nginx restart
