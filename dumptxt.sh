#!/bin/bash
for file in `ls ./dmp/*.dmp`
do
	echo $file
	#filename="${file%.*}"
	#echo "file name is ${filename}"
	./tool/minidump_stackwalk $file ./symbols/ > `echo "${file%.*}.txt"`
	mv ${file%.*}.txt ./house
done
