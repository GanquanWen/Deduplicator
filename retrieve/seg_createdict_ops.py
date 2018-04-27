import hashlib
import os
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
    #create artile list file
    article_hash_lst_filename = path+'list_'+os.path.basename(filename)
    article_hash_lst_file=open(article_hash_lst_filename,'w')
    article_hash_lst_file.write(str(article_hash_lst).strip('[').strip(']'))
    return article_hash_lst

#test:
#test was done in folder:seg_createdict_ops
def main():
    dic={}
    segment_create_dict('org_file_a.txt',1,dic,'test/')
    #segment_create_dict('seg_createdict_ops/file2.txt',1,dic,'seg_createdict_ops/Lockers/')
    #segment_create_dict('seg_createdict_ops/file3.txt',1,dic,'seg_createdict_ops/Lockers/')
    #print(dic)

if __name__ == '__main__':
    main()
    



