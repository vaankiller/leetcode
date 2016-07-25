#!/bin/sh 

count=0

while read line
do
	count=`expr $count + 1`
	if [ $count -eq 10 ]
	then
		echo $line
	fi
done < ./file.txt

# Tips:
# use while loop, because for loop ifs will be "space"",\n,...
# airthmetic in shell use expr, in if condition ues -eq not ==
# read file in shell 
