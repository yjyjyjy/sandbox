#!/bin/bash
cd /home/ubuntu/stable-diffusion-webui-docker
docker compose --profile auto up --build > /home/ubuntu/tmpOut.txt

var=`cat tmpOutput.txt | awk '/Running on public URL: / {printf $7}'`
echo $var