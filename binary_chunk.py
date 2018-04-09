def binary_chunk(file_name):
    with open(file_name, 'r') as f:
        s=f.read()
    cnt=0
    offset=0
    #window_length=10000
    window_length=10
    ori=s
    psed_para=[]
    for i in range(0,len(s),1):
        window_content=s[i:i+window_length]
        print(window_content)
        slide_step=2
        if window_content[-slide_step:]=='10':
            cnt=cnt+1
            #record this point,get a list of inserting \n point
            psed_point=i+window_length-1
            psed_para.append(psed_point)
    print(psed_para)
    for p in psed_para:
        print(ori[p])
        ori=insert(ori,'a',p+1+offset)
        offset+=1
    #print(ori) 
    ori=ori.replace('a','\n')
    print(ori)
    new_file = open(file_name, "w")
    new_file.write(ori)
    new_file.close()
       
def insert(original,new,position):
    return original[:position] + new + original[position:]

binary_chunk('test3 copy.txt')
