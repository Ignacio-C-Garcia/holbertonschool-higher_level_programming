#!/bin/bash
#comment
if [ $(curl -o -I -L -s -w "%{http_code}" "$1") -eq 200 ]; then curl -L "$1"; fi
