import numpy as np

if __name__ == "__main__":
	data = []
	data.append(np.array([[1,1,0,0]]))
	data.append(np.array([[0,0,1,1]]))
	data.append(np.array([[0,1,1,0]]))

	result = np.zeros((4,4))
	for a in data:
		print(np.dot(a.T,a))
		result += np.dot(a.T , a)
	print(result)
