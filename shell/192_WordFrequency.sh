#!/usr/bin/env bash

tr -s ' ' '\n' | grep -v '^$' | sort | uniq -c | sort -nr | awk '{print $2" "$1}'
