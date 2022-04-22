#!/bin/bash
#comment
curl -sI $1 | grep "Content-Lenght" | cut -d " " -f 2
