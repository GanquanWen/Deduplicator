## Copyright 2018 Ganquan Wen wengq@bu.edu


import sys


def retrieve(file, path):
	'''get the list of hash
	   then retrieve the file according to hash in order
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

	original_file = ""
	for part in parts_list:
		part_file = open(path+'example/'+part+'.txt', "r")
		line = part_file.readline()
		while line:
			original_file += line
			line = part_file.readline()
		original_file += '\n'
		part_file.close()

	output_file = open(path+'org_'+file, "w")
	output_file.write(original_file)
	output_file.close()

	return original_file


def main():
	file = 'file_a.txt'
	path = ''
	print retrieve(file, path)


if __name__ == '__main__':
	main()
