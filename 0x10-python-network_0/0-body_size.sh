#!/bin/bash
#a Bash script that takes in a URL and return content:type
echo $(curl $1 -sI | grep -i Content-Length | awk '{print $2}')