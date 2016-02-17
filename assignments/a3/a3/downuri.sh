#!/bin/bash
dataDir="../webpages/"
rm -f hashtable
touch hashtable
counter=0
for line in `cat url_list.txt`; do
	fname=`echo -n $line | openssl md5 | cut -d" " -f2`
	curl  --silent -A "Mozilla/5.0 (X11; Linux i686 (x86_64); rv:2.0b4pre) Gecko/20100812 Minefield/4.0b4pre" "$line" > ${dataDir}${fname}
	echo -e $fname"\t"$line >>hashtable
	counter=$[$counter+1]
	percent=$[$counter/10]
	echo -e -n "\r"$percent"%"
done