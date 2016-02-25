from pygraphml import Graph
from pygraphml import GraphMLParser
import numpy
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
parser=GraphMLParser()
g=parser.parse("mln.graphml")

#g.show()
datafile=open("facebook.data","w")
dropfile=open("facebook_dropped.data","w")
nodes = g.nodes()
friendCounts=[]
for node in nodes:
	try:
		count=node['friend_count']
    		friendCounts.append(int(count)) 
	except Exception, e:
		dropfile.write(str(node)+"\n")

friendCounts.append(len(nodes)) 
friendCounts=sorted(friendCounts)
datafile.write("Friend_count\t"+str(len(nodes))+"\n")
datafile.write("std\t"+str(numpy.std(friendCounts))+"\n")
datafile.write("mean\t"+str(numpy.mean(friendCounts))+"\n")
datafile.write("median\t"+str(numpy.median(friendCounts))+"\n")
for fcount in friendCounts:
	datafile.write(str(fcount)+"\n")
datafile.close()
dropfile.close()