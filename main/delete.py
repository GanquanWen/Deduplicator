## Copyright 2018 Ganquan Wen wengq@bu.edu


import os


def delete(file, path):
	'''get the list of hash
	   then delete every part on the list according to hash in order
	'''
	M = get_iven('Inven_dic.txt','')
	file_name = 'list_' + file

	# f = open(path+file_name, "r")
	# line = f.readline()
	# parts_list = []
	# while line:
	# 	line = line.rstrip("\n")  # delete the \n at the end of each line
	# 	parts_list.append(line)
	# 	print(line)
	# 	line = f.readline()
	# f.close()
	f = open(path+file_name, "r")
	line = f.readline()
	f.close()
	org_list = line.split(", ")
	parts_list = []
	for n in range(len(org_list)):
		parts_list.append(org_list[n].strip("\'"))

	for part in parts_list:
		if part in M:
			if len(M[part]) == 1:
				os.remove(path+part+'.txt')
				print('remove '+path+part+'.txt')
				del M[part]
			else:
				if file in M[part]:
					M[part].remove(file)
		else:
			continue

	os.remove(path+file_name)
	print (file + ' deleted')
	
	dic = M
	Inven_dic=open('Inven_dic.txt','w')
	for key in dic:
		info="{} ".format(key)
		Inven_dic.write(str(info))
		for child in range(0,len(dic[key])):
			info="{} ".format(dic[key][child])
			Inven_dic.write(str(info))
		Inven_dic.write('\n')

	return M


def get_iven(file, path):
	'''get the list of hash
	   then retrieve the file according to hash in order
	'''
	f = open(path+file, "r")
	line = f.readline()
	parts_list = []
	while line:
		line = line.rstrip("\n")  # delete the \n at the end of each line
		parts_list.append(line)
		#print (line)
		line = f.readline()
	f.close()
	#print(parts_list)
	inventory = {}
	for i in range(len(parts_list)):
		parts_list[i] = parts_list[i].split()
		inventory[parts_list[i][0]] = []
		for k in range(1, len(parts_list[i])):
			inventory[parts_list[i][0]].append(parts_list[i][k])
	return inventory


def main():
	dic = get_iven('Inven_dic.txt','')
	# print('Inventory restored')
	# print(dic)

	file = 'file_c.txt'
	path = 'locker/'
	dic = delete(file, path, dic)
	


if __name__ == '__main__':
	main()