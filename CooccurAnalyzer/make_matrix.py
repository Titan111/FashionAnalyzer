import numpy as np

def make_itr_dict(file_name):
	f = open(file_name,"r")
	itr = 0
	itr_dict = {}
	for line in f:
		itr_dict[line.strip()] = itr
		itr += 1
	return itr_dict

if __name__ == "__main__":
	f = open("data/iqon_tags.ssv","r")
	itr_dict = make_itr_dict("data/selected_tags2.txt")
	
	N = 76
	result = np.zeros((N,N))

	for line in f:
		tags = line.strip().split(" ")
		vector = np.zeros((N,1))
		for tag in tags:
			if tag in itr_dict:
				vector[itr_dict[tag]][0] = 1
		result += np.dot(vector,vector.T)
	f.close()
	np.savetxt("result.csv",result,delimiter=",")


