#!/bin/bash

ls -l
x=10
y=20
z=$((x+y))
echo $z


who 
echo ""

hostnamectl
echo ""

uptime 
echo ""

df -h
echo ""

free -m
echo ""

date
echo ""



if [ -f "/home/mr-arthor/Desktop/script.sh" ]; then
    echo "File exists."
else
    echo "File does not exist."
fi
echo -e "\n"
# for loop
for name in Alice Bob Charlie; do
    echo "Hello, $name!"
done

# while loop

echo -e "\n"

count=1
while [ $count -le 5 ]; do
    echo "Count using while: $count"
    count=$((count + 1))
done

echo -e "\n"

# until loop

count=1
until [ $count -gt 5 ]; do
    echo "Count:using until $count"
    count=$((count + 1))
done