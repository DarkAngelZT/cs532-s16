#!/bin/bash
curl --silent "http://f-measure.blogspot.com/" > rawBlogs/blog001
curl --silent "http://ws-dl.blogspot.com/" > rawBlogs/blog002
rm -f rawBlogs/uriList
touch rawBlogs/uriList
echo "blog001 http://f-measure.blogspot.com/" >> rawBlogs/uriList
echo "blog002 http://ws-dl.blogspot.com/" >> rawBlogs/uriList
for (( i = 3; i <= 350; i++ )); do
	num=`seq -f%03g $i $i`
	uri=`curl -Ls -o  rawBlogs/blog$num -w %{url_effective} "https://www.blogger.com/next-blog?navBar=true&blogID=3471633091411211117"`
	
	echo "blog$num $uri" >> rawBlogs/uriList
done
#remove duplicate uri and page files
sort -u -k2 rawBlogs/uriList > rawBlogs/uriListTmp
sort -k1 rawBlogs/uriListTmp> rawBlogs/uriList
rm rawBlogs/uriListTmp
for file in `cat rawBlogs/uriList | cut -d' ' -f1`; do
	mv rawBlogs/$file rawBlogs/pages/
done