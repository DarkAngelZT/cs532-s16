from local import cd
import json
import datetime
time_now=datetime.datetime.now()
data=open("../../momento.list")
outputf=open('../../cd.list','w')
strline=data.readlines()
counter=0
for line in strline:
	col=line.split('\t')
	memento=int(col[1])
	if memento>0:
		r=cd(col[0])
		re=json.loads(r)
		if re['Estimated Creation Date'] != '':
			createTime=datetime.datetime.strptime(re['Estimated Creation Date'],'%Y-%m-%dT%H:%M:%S')
			deltaTime=time_now-createTime
			outputf.write(str(deltaTime.days)+"\t"+str(col[1]).strip()+"\n")
	counter=counter+1
	print(str(counter/10.0)+"%")
data.close()
outputf.close()