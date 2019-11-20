#!/usr/bin/env bash

source_dir="inputData"

hadoop fs -rm -r -f -skipTrash $source_dir output
hadoop fs -put $source_dir/ .
hadoop jar $1.jar $1 $source_dir output

hadoop fs -getmerge -nl output collectedResults 
#You can add -nl to enable adding newline char after the end of each file
echo cat collectedResults

