#!/bin/bash
for file in `ls ./libso/*.so`
do
	echo $file
	./tool/dump_syms $file  > `echo "${file}.sym"`
done
