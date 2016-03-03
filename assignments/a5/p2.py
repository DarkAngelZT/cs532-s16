from igraph import *
g=Graph.Read_GraphML("karate.GraphML")
layout=g.layout('fr')

for c in range(3,6):
	cut_graph=g.community_edge_betweenness(clusters=c,directed=False,weights=g.es['weight'])
	cutted_g=cut_graph.as_clustering()

	plot(cutted_g,"p2_cluster"+str(c)+".pdf",layout=layout,vertex_label=g.vs['name'])
