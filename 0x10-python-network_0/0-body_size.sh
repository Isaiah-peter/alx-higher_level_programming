#!/bin/bash
#a Bash script that takes in a URL,
#sends a request to that URL, and
#displays the size of the body of the response

p=$(curl $1 -sI | grep -i Content-Length | awk '{print $2}')
echo $p