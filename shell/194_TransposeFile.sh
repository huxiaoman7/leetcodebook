#!/usr/bin/env bash

awk '{
    for (i = 1; i <= NF; i++) {
        value[NR, i] = $i
    }
    if (NF > columns) {
        columns = NF
    }
}
END {
    for (i = 1; i <= columns; i++) {
        line = value[1, i]
        for (j = 2; j <= NR; j++) {
            line = line" "value[j, i]
        }
        print line
    }
}'
