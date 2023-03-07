#!/bin/bash
apt update
apt install apache2 -y
ufw allow 'Apache'
Uff enable
echo "<body><h1>User id: $(whoami) on Server $(hostname -l) at `date`</h1></body>" > /var/www/html/index.html