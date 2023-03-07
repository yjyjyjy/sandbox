#!/bin/bash
/bin/ec2metadata >meta
prefix="instance-id: "
while IFS= read -r line
do
        if [[ "$line" == *"instance-id"* ]]
        then
                id=${line#"$prefix"}
        fi
done <meta
cmd=$(curl -d '{"instanceId":"ak47"}' -H "Content-Type: application/json" -X POST https://a1-rouge.vercel.app/api/instance/register)
echo $id