#!/bin/bash
while [ true ];do
    read -t 3 -n 1
    if [ $? = 0 ];then
        python find_brick.py
    fi
done