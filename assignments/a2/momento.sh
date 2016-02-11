#!/bin/bash
rm -f momento.list
touch momento.list
prefix="http://mementoproxy.cs.odu.edu/aggr/timemap/link/1/"
counter=0
num=0
rm -rf tmpdir
mkdir tmpdir
function getUrlCount()
{
	local fid=`date +%s`
	local curNum
	local ts
	local nurl
	curl --silent "$1" > tmpdir/tmp$fid
	curNum=`cat tmpdir/tmp$fid | egrep 'rel="[^"]*memento[^"]*"' | wc -l`
	num=$[$curNum+$num]
	if [[ $curNum -gt 0 ]]; then
		for ts in `cat tmpdir/tmp$fid | grep -o '<[^>]*>;rel="timemap"'`; do
			nurl=`echo -n $ts |  awk -F"[<>]" '{print $2}'`
			if [[ "$nurl" != '' ]]; then
				getUrlCount "$nurl"
			fi
		done
	fi
}

for line in `cat url_list.txt`; do
	curl --silent "${prefix}${line}"> tmpdir/tmp
	num=`cat tmpdir/tmp | egrep 'rel="[^"]*memento[^"]*"' | wc -l`
	if [[ $num -gt 0 ]]; then
		for timemap in `cat tmpdir/tmp | grep -o '<[^>]*>;rel="timemap"'`; do
			newurl=`echo -n $timemap |  awk -F"[<>]" '{print $2}'`
			if [[ "$newurl" != '' ]]; then
				getUrlCount "$newurl"
			fi
		done
	fi
	echo -e $line"\t"$num >>momento.list
	counter=$[$counter+1]
	percent=$[$counter/10]
	echo -e -n "\r"$percent"%"
done
rm -rf tmpdir
