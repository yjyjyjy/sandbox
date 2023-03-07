#! /bin/bash
FILE="tempOutput"
echo 123asdf 1>$FILE
echo azxcv2rqw23kasdjfk 1>>$FILE
echo 3 1>>$FILE
echo 45azf 1>>$FILE
while IFS= read -r line
do
  if [[ "$line" == *"2rqw23"* ]]
  then
    echo "$line"
  fi
done <"$FILE"