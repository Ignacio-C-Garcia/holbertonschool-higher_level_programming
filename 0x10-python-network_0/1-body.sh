#!/bin/bash
#comment
http=$(curl -o -I -L -s -w "%{http_code}" "$1")
if [ "$http" -eq 200 ]; then
curl -L "$1"
fi
