## Copyright 2018 Ganquan Wen wengq@bu.edu


import sys


def retrieve(file, path):
	'''get the list of hash
	   then retrieve the file according to hash in order
	'''
	file_name = 'list_' + file
	f = open(path+file_name, "r")
	line = f.readline()
	f.close()
	org_list = line.split(", ")
	parts_list = []
	for n in range(len(org_list)):
		parts_list.append(org_list[n].strip("\'"))

	'''retrieve each part of the original article by the hash
	   connect them to make a string'''

	original_file = ""
	for i in range(len(parts_list)):
		part_file = open(path+parts_list[i]+'.txt', "r")
		line = part_file.readline()
		while line:
			original_file += line
			line = part_file.readline()
		# if i < len(parts_list)-1:
		# 	original_file += '\n\n'  # adding a blank line between each part
		part_file.close()

	'''store the article as txt file'''
	file_name = file.lstrip('list_')
	file_name = file_name.rstrip('.txt')
	output_file = open(file_name+'_retrieved.txt', "w")
	output_file.write(original_file)
	output_file.close()

	return original_file


def main():
	file = 'org_file_a.txt'
	path = 'test/'
	# print(retrieve(file, path))


if __name__ == '__main__':
	main()
