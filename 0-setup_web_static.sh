#!/usr/bin/env bash
# sets up your web servers for the deployment of web_static
sudo apt-get update -y
sudo apt-get -y install nginx
mkdir -p data/web_static/releases/test/
mkdir -p data/web_static/shared/
sudo chmod -R 777 data/web_static/releases/test/
printf "<html>
  <head>
  </head>
  <body>
     Holberton School
  </body>
</html>" | sudo tee data/web_static/releases/test/index.html
ln -sf data/web_static/releases/test data/web_static/current
sudo chown -R ubuntu:ubuntu data/ 
sudo sed -i '/listen 80 default_server;/a locacion /hbnb_static {alias /data/web_static/current: autoindex off; }' /etc/nginx/sites-available/default 
sudo service nginx start
