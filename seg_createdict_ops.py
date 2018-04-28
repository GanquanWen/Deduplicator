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
def segment_create_dict(filename, dic, path):
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
        # print(tmp2)
        ###
        hashstr = tmp2.encode('utf-8')
        hashtmp = para_hash(hashstr)
        article_hash_lst.append(hashtmp)
        if hashtmp in dic:
            if os.path.basename(filename) not in dic[hashtmp]:
                dic[hashtmp].append(os.path.basename(filename))
        else:
            chunkname = path + hashtmp + ('.txt')

            #dic[hashtmp] = [os.path.basename(filename)]
            dic[hashtmp] = [os.path.basename(filename)]
            text_file = open(chunkname, "w")
            text_file.write(tmp2)
            text_file.close()
    #create artile list file
    article_hash_lst_filename = path+'list_'+os.path.basename(filename)
    article_hash_lst_file=open(article_hash_lst_filename,'w')
    article_hash_lst_file.write(str(article_hash_lst).strip('[').strip(']'))
    return article_hash_lst

def binary_chunk(filename,dic,path):
    with open(filename, 'r') as myfile:
        s = myfile.read()
    size = len(s)
    #print(size)
    article_hash_lst = []
    if size < 100000:
        window_length = size // 100
        pattern = '101'
    else:    
        window_length = 2000
        pattern = '010101'
    step = 1
    flag = 0 
    #for i in range(0,len(s),step):
    i = 0
    tmpi = 0
    while i < len(s):
        if flag == 1:
            i += window_length-1
            tmpi = i
        window_content = s[tmpi:i+window_length]
        slide_step = len(pattern)
        if window_content[-slide_step:] == pattern:
            flag = 1
            hashstr = window_content.encode('utf-8')
            hashtemp = para_hash(hashstr)
            article_hash_lst.append(hashtemp)
            if hashtemp in dic:
                if os.path.basename(filename) not in dic[hashtemp]:
                    dic[hashtemp].append(os.path.basename(filename))
            else:
                chunkname = path + hashtemp + ('.txt')
                dic[hashtemp] = [os.path.basename(filename)]
                text_file = open(chunkname, "w")
                text_file.write(window_content)
                text_file.close()
        else:
            flag = 0

        i += 1
    article_hash_lst_filename = path+'list_'+os.path.basename(filename)
    article_hash_lst_file=open(article_hash_lst_filename,'w')
    article_hash_lst_file.write(str(article_hash_lst).strip('[').strip(']'))
    return article_hash_lst

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
        print(parts_list[i])
        inventory[parts_list[i][0]] = []
        for k in range(1, len(parts_list[i])):
            inventory[parts_list[i][0]].append(parts_list[i][k])
    return inventory


#test:
#test was done in folder:seg_createdict_ops
def main():
    filename = 'seg_createdict_ops/binary/file3.txt'
    with open(filename, 'r') as myfile:
        data = myfile.read()
    tmp = data.split('\n\n')
    if len(tmp) > 1:
        inv = 'Inven_dic.txt'
        try:
            dic_a = get_iven('Inven_dic.txt','')
        except:
            dic_a = {}
        dic = dic_a 
    else:
        inv = 'Inven_dic_binary.txt'
        try:
            dic_b = get_iven('Inven_dic_binary.txt','')
        except:
            dic_b = {}
        dic = dic_b 
    # segment_create_dict('seg_createdict_ops/file1.txt',dic,'seg_createdict_ops/Lockers/')
    # segment_create_dict('seg_createdict_ops/file2.txt',dic,'seg_createdict_ops/Lockers/')
    # segment_create_dict('seg_createdict_ops/file3.txt',dic,'seg_createdict_ops/Lockers/')
    #binary_chunk(filename,dic_b,'seg_createdict_ops/Lockers2/')
    binary_chunk(filename,dic_b,'seg_createdict_ops/Lockers2/')

    Inven_dic=open(inv,'w')
    for key in dic:
        info="{} ".format(key)
        Inven_dic.write(str(info))
        for child in range(0,len(dic[key])):
            info="{} ".format(dic[key][child])
            Inven_dic.write(str(info))
        Inven_dic.write('\n')

    
if __name__ == '__main__':
    main()







