import hashlib
#hash the given string
def para_hash(string):
    h=hashlib.sha256()
    h.update(string)
    result=h.hexdigest()
    return result

#segment a file into paragraphs
#step:current set to 10(10 paragraphs as a chunk)
#about the dictionary:
#    key:hash code of this segment(filename)
#    value:[0]location, [1]:a list contains its childs(aka raw filenames contain this paragraph)
#This function returns a list that contains all hash code of this article
def segment_create_dict(filename, step, dic, path):
    '''
    read from file
    create and renew the dictionary
    write chunks to file in current path
    '''
    article_hash_lst = []
    with open(filename, 'r') as myfile:
        data = myfile.read()
    tmp = data.split('\n\n')
    length = len(tmp)
    for i in range(0,length,step):
        tmp2 = ''
        if i + step < length:
            for j in range(i,i + step):
                tmp2 += tmp[j]
        else:
            for j in range(i,length):
                tmp2 += tmp[j]
        # print(tmp2)
        ###
        hashstr = tmp2.encode('utf-8')
        hashtmp = para_hash(hashstr)
        article_hash_lst.append(hashtmp)
        if hashtmp in dic:
            dic[hashtmp][1].append(filename)
        else:
            chunkname = path + hashtmp + ('.txt')
            dic[hashtmp] = [path,[filename]]
            text_file = open(chunkname, "w")
            text_file.write(tmp2)
            text_file.close()
    return article_hash_lst

#run:
'''
dic={}
a=segment_create_dict('file1.txt',10,dic,'')
'''
