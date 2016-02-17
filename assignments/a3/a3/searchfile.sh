#!/bin/bash
dataDir="../webpage_processed/"
fileCount=0
rm -f TFdata
touch TFdata
amount=`grep -rl "$1" $dataDir| wc -l`
IDF=$(echo "scale=6;30000000000000/3970000000"|bc)
IDF=`echo $IDF | awk '{printf("%.6f",log($1)/log(2))}'`
for file in `ls $dataDir`; do
	count=`cat ${dataDir}${file} | grep -o "$1" | wc -l`
	if [[ $count -gt 0 ]]; then
		words=`cat ${dataDir}${file} | wc -w`
		TF=$(echo "scale=6;$count/$words"|bc)
		TFIDF=`echo "scale=6;$TF*$IDF"| bc`
		url=`grep "$file" hashtable | cut -f2`
		echo -e $TFIDF"\t"$TF"\t"$IDF"\t"$url >> TFdata
		fileCount=$[$fileCount+1]
		if [[ $fileCount -gt 20 ]]; then
			break
		fi
	fi
done
sort -r -n -k1 TFdata > TFRankdata
rm TFdata