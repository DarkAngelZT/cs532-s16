import os
import json
# import sys
# reload(sys)
# sys.setdefaultencoding('utf-8')

nameFile=open('followers_name.txt')
genderFile=open('gender.txt','w')
droppedlog=open('p2_dropped.txt','w')
strline=nameFile.readlines()
for line in strline:
	try:
		firstname=line.split(' ')[0]
		genderobj=json.load(os.popen('GET https://api.genderize.io/?name="%s"'%firstname))
		gender=genderobj['gender']
		if 'null' in gender:
			droppedlog.write(line)
		else:
			genderFile.write(line.strip()+'\t'+gender+'\n')
	except Exception, e:
		droppedlog.write(line)
		continue
	
nameFile.close()
genderFile.close()
droppedlog.close()