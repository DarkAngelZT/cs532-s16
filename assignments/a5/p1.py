from igraph import *
g=Graph.Read_GraphML("karate.GraphML")
layout=g.layout('fr')
plot(g,'p1_org.pdf',layout=layout,vertex_label=g.vs['name'])
color_table={1:"blue",2:'red'}
g.vs['color']=[color_table[group] for group in g.vs['Faction']]
plot(g,'p1_org_split.pdf',layout=layout,vertex_label=g.vs['name'])

cut_graph=g.community_edge_betweenness(clusters=2,directed=False,weights=g.es['weight'])
cutted_g=cut_graph.as_clustering()

plot(cutted_g,"p1_cut.pdf",layout=layout,vertex_label=g.vs['name'])