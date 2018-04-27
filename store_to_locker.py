import hashlib
def is_binary(s):
	try:
		int(s[0])
		int(s[-13])
		return True
	except:
		return False
def binary_chunk(s,step,dic,path,filename):
	articlelist = []
	cnt=0
	offset=0
	window_length=10000
	ori=s
	psed_para=[]
	for i in range(0,len(s),step):
		window_content=s[i:i+window_length]
		slide_step=6
		if window_content[-slide_step:]=='010101':
			hashtemp = hash(window_content)
			print(hashtemp)
			articlelist.append(hashtemp)
			if hashtemp in dic:
				dic[hashtemp][1].append(filename)
			else:
				chunkname = path + hashtemp + ('.txt')
				dic[hashtemp] = [path,[filename]]
				text_file = open(chunkname, "w")
				text_file.write(window_content)
				text_file.close()
	#         hashstr = window_content.encode('utf-8')
	#         hashtmp = para_hash(hashstr)
	#         article_hash_lst.append(hashtmp)
	#         psed_point=i+window_length-1
	#         psed_para.append(psed_point)
	# for p in psed_para:
	#     ori=insert(ori,'a',p+1+offset)
	#     offset+=1
	# ori=ori.replace('a','\n')
	# new_file = open('ec504_sample_file/binaryA.txt', "w")
	# new_file.write(ori)
	# new_file.close()
def segment_create_dict(s,dic,path,filename):
	'''
	read from file
	create and renew the dictionary
	write chunks to file in current path
	'''
	article_hash_lst = []
	tmp = s.split('\n\n')
	length = len(tmp)
	if length < 1000:
			step = 1
	else:
		step = length//1000
	for i in range(0,length,step):
		tmp2 = ''
		if i + step < length:
			for j in range(i,i + step):
				tmp2 += tmp[j]
		else:
			for j in range(i,length):
				tmp2 += tmp[j]
				hashtmp = hash(temp2)
				article_hash_lst.apend(hashtmp)
				if hashtmp in dic:
					dic[hashtmp][1].append(filename)
				else:
					chunkname = path + hashtmp + ('.txt')
					dic[hashtmp] = [path,[filename]]
					text_file = open(chunkname, "w")
					text_file.write(tmp2)
					text_file.close()
	return article_hash_lst
def insert(original,new,position):
	return original[:position] + new + original[position:]
def para_hash(string):
	h=hashlib.sha256()
	h.update(string)
	result=h.hexdigest()
	return result
def hash(chunk):
	hashstr = chunk.encode('utf-8')
	hashtmp = para_hash(hashstr)
	return hashtmp
def main():
	dic = {}
	filename = 'test1_binary.txt'
	path = 'output/'
	f= open(filename,'r') 
	s= f.read()
	if is_binary(s):
		binary_chunk(s,30,dic,path,filename)
	else:
		seg_createdict_ops(s,dic,path,filename)
main()
