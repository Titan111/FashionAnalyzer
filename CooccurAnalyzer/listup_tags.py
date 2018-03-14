import matplotlib.pyplot as plt

#zipfの法則確認用
def plot(tag_ranking):
		freq_list = list(map(lambda x:x[1],tag_ranking))
		plt.xscale("log")
		plt.yscale("log")
		plt.plot(range(1,len(freq_list)+1),freq_list)
		plt.show()

def make_freq_dict(file_name):
	f = open(file_name, "r")
	tag_dict = {}
	for line in f:
		tag_list = line.strip().split(" ")
		for tag in tag_list:
			if tag in tag_dict:
				tag_dict[tag] += 1
			else:
				tag_dict[tag] = 1
	f.close()
	return tag_dict

def make_set(file_name):
	f = open(file_name, "r")
	tag_set = set()
	for line in f:
		tag_list = line.strip().split(" ")
		for tag in tag_list:
			tag_set.add(tag)
	f.close()
	return tag_set

if __name__ == "__main__":
	tag_dict = make_freq_dict("iqon_tags.ssv")
	tag_ranking = sorted(tag_dict.items(),key=lambda x:x[1],reverse=True)
	
	for tag in tag_ranking:
		print(tag[0],"\t",tag[1])
