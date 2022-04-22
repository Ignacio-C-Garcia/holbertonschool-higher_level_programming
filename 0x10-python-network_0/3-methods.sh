#!/bin/bash
#comment
curl -sI $1 | grep "Allow" | cut -d " " -f 2-
