#!/usr/bin/env bash
# sets up your web servers for the deployment of web_static
sudo apt-get update -y
sudo apt-get -y install nginx
sudo chmod -R 777 /var/www/html/
sudo echo "Hello World" | sudo tee /var/www/html/index.html
sudo sed -i '/server_name _;/a rewrite ^/redirect_me/ https://www.youtube.com/watch?v=QH2-TGUlwu4 permanent;' /etc/nginx/sites-available/default
sudo echo "Ceci n'est pas une page" | sudo tee /var/www/html/page.html
sudo sed -i '/server_name _;/a error_page 404 /page.html;' /etc/nginx/sites-available/default
var=$(cat /proc/sys/kernel/hostname)
sudo sed -i '/http {/a add_header X-Served-By '"${var}"';' /etc/nginx/nginx.conf
sudo mkdir -p /data/web_static/releases/test/
sudo mkdir -p /data/web_static/shared/
sudo touch /data/web_static/releases/test/index.html
echo "<html>
  <head>
  </head>
  <body>
     Holberton School
  </body>
</html>" | sudo tee /data/web_static/releases/test/index.html
sudo ln -sf /data/web_static/releases/test /data/web_static/current
sudo chown -R ubuntu:ubuntu /data/ 
sudo sed -i '/listen 80 default_server;/a locacion /hbnb_static {alias /data/web_static/current: autoindex off; }' /etc/nginx/sites-available/default 
sudo service nginx start
