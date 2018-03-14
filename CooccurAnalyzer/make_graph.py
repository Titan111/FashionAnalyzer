from graphviz import Graph
import numpy as np

def make_itr_dict(file_name):
	f = open(file_name,"r")
	itr = 0
	itr_dict = {}
	for line in f:
		itr_dict[line.strip()] = itr
		itr += 1
	return itr_dict

def make_tag_list(file_name):
	f = open(file_name,"r")
	tag_list = []
	for line in f:
		tag_list.append(line.strip())
	return tag_list

if __name__ == "__main__":
	itr_dict = make_itr_dict("data/selected_tags2.txt")
	tag_list = make_tag_list("data/selected_tags2.txt")

	G = Graph(format="png")
	G.attr("node",shape="circle")

	N = 76
	for name in tag_list:
		G.node(name,name)

	for start in range(N):
		for end in range(start+1,N):
			G.edge(tag_list[start],tag_list[end])

	print(G)
#	G.render("a")
