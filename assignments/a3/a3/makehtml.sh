#!/bin/bash
dataDir="../webpage_processed/"
raw_dir="../webpages/"
counter=0
for line in `cat url_list.txt`; do
	fname=`echo -n $line | openssl md5 | cut -d" " -f2`
	lynx  -dump -force_html ${raw_dir}${fname} > ${dataDir}${fname}
	counter=$[$counter+1]
	percent=$[$counter/10]
	echo -e -n "\r"$percent"%"
done