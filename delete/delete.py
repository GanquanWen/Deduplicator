## Copyright 2018 Ganquan Wen wengq@bu.edu


import os


def delete(file, path, M):
	'''get the list of hash
	   then delete every part on the list according to hash in order
	'''
	f = open(path+file, "r")
	line = f.readline()
	parts_list = []
	while line:
		line = line.rstrip("\n")  # delete the \n at the end of each line
		parts_list.append(line)
		print line
		line = f.readline()
	f.close()

	for part in parts_list:
		if len(M[part][1]) == 1:
			os.remove(path+'example/'+part+'.txt')
			del M[part]
		else:
			M[part][1].remove(file)

	os.remove(path+file)
	print M

	return None


def main():
	file = 'file_a.txt'
	path = ''
	M = {}
	M['37846273894736472861a7cb3c2d4a71'] = [path, ['file_a.txt']]
	M['37846273894736472861a7cb3c2d4a72'] = [path, ['file_a.txt']]
	M['37846273894736472861a7cb3c2d4a73'] = [path, ['file_a.txt']]
	M['37846273894736472861a7cb3c2d4a74'] = [path, ['file_a.txt']]
	M['37846273894736472861a7cb3c2d4a75'] = [path, ['file_a.txt', 'file_b.txt']]

	delete(file, path, M)


if __name__ == '__main__':
	main()