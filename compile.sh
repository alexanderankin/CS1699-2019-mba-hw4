#!/usr/bin/env bash

echo 'javac -cp $HADOOP_CLASSPATH:acommons-cli-1.2.jar WordCount2.java -d WordCount2'
javac -cp $HADOOP_CLASSPATH:acommons-cli-1.2.jar $1.java -d $1

echo "jar cvf $1.jar -C $1/ ."
jar cvf $1.jar -C $1/ .
