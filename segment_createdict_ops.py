import hashlib
def file_hash(filename):
    h = hashlib.sha256()
    with open(filename, 'rb', buffering=0) as f:
        for b in iter(lambda : f.read(128*1024), b''):
            h.update(b)
    return h.hexdigest()

#segment a file in to paragraphs
#series：file series,for example:f1
#need further operation: judge if a segment in the dict,if it is than no need to store
def chunk_to_file(data,series,step):
    '''
    write paragraphs into files
    '''
    tmp = data.split('\n\n')
    length = len(tmp)
    num = 1
    for i in range(0,length,step):
        tmp2 = ''
        if i + step < length:
            for j in range(i,i + step):
                tmp2 += tmp[j]
        else:
            for j in range(i,length):
                tmp2 += tmp[j]
        filename = (series+'_') + str(num) + ('.txt')
        text_file = open(filename, "w")
        text_file.write(tmp2)
        text_file.close()
        num += 1

#hash_lst:list with all the hash codes，need further operation to write them to a file.
def create_para_dict(filename,M,loc,hash_lst):
    '''
    key:hash code of this segment(filename)
    value:[0]location, [1]:a list contains its childs(aka filenames contain this paragraph)
    '''
    with open(filename, 'r') as myfile:
        p = myfile.read()
        hashtmp = file_hash(filename)
        if hashtmp in M:
            M[hashtmp][1].append(filename)
        else:
            M[hashtmp] = [loc,[filename]]
    hash_lst.append(hashtmp)
'''
with open('file1.txt', 'r') as myfile:
    data = myfile.read()
chunk_to_file(data,'f1',10)'''


#segment a file in to paragraphs
#series：file series,for example:f1
#need further operation: judge if a segment in the dict,if it is than no need to store
def chunk_to_file(data,series,step):
    '''
    write paragraphs into files
    '''
    tmp = data.split('\n\n')
    length = len(tmp)
    num = 1
    for i in range(0,length,step):
        tmp2 = ''
        if i + step < length:
            for j in range(i,i + step):
                tmp2 += tmp[j]
        else:
            for j in range(i,length):
                tmp2 += tmp[j]
        filename = (series+'_') + str(num) + ('.txt')
        text_file = open(filename, "w")
        text_file.write(tmp2)
        text_file.close()
        num += 1

#hash_lst:list with all the hash codes，need further operation to write them to a file.
def create_para_dict(filename,M,loc,hash_lst):
    '''
    key:hash code of this segment(filename)
    value:[0]location, [1]:a list contains its childs(aka filenames contain this paragraph)
    '''
    with open(filename, 'r') as myfile:
        p = myfile.read()
        hashtmp = file_hash(filename)
        if hashtmp in M:
            M[hashtmp][1].append(filename)
        else:
            M[hashtmp] = [loc,[filename]]
    hash_lst.append(hashtmp)
'''
with open('file1.txt', 'r') as myfile:
    data = myfile.read()
chunk_to_file(data,'f1',10)'''

'''
para_dict = {}
hash_lst=[]
for i in lst:
    create_para_dict(i,para_dict,'aaa',hash_lst)
'''