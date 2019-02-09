#!/bin/bash
for i in {1..10}
do
        mkdir "dir$i"
        top -o +%CPU | awk "NR==(($i+7))" > dir$i/file$i
done
