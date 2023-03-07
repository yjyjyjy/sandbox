#!/bin/bash
URL=""
while true
do
  URL=`cat tmpOutput.txt | awk '/Running on public URL: / {printf $7}'`
  if [ "$URL" != "" ]
  then
    echo $URL
    break
  else
    sleep 1
  fi
  # while IFS= read -r line
  # do
  #         if [[ "$line" == *"Running on public URL:"* ]]
  #         then
  #                 id=${line#"$prefix"}
  #         fi
  # done <meta
done