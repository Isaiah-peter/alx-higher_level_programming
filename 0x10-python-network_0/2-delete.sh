#!/bin/bash
#delete body
echo $(curl $1 -s -X DELETE)
