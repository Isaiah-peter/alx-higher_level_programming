#!/bin/bash
#list allowed HTTP method
curl -s -I "$1" | grep Allow | cut -d' ' -f2-