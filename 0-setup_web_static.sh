#!/usr/bin/env bash
# Prepare Web Server
apt-get update -y
apt-get install nginx -y
mkdir -p /data/web_static/shared/
mkdir -p /data/web_static/releases/test/
echo "Holberton School" > /data/web_static/releases/test/index.html
rm -rf /data/web_static/current
ln -sf /data/web_static/releases/test/ /data/web_static/current
chown -R ubuntu:ubuntu /data/

cont="server_name _;\n\t"

loc="location \/hbnb_static\/ {\n\t\talias \/data\/web_static\/current\/;\n\t\tautoindex off;\n\t}"

sed -i "s/server_name _;/$cont$loc/" /etc/nginx/sites-available/default
service nginx restart
exit 0
