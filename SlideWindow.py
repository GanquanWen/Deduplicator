def binary_chunk(file_name):
    with open(file_name, 'r') as f:
        s=f.read()
    #print(s[0:5])
    #print(s)
    cnt=0
    window_length=10000
    ori=s
    for i in range(0,len(s),6):
        window_content=s[i:i+window_length]
        #print(window_content)
        if window_content[-8:]=='10101010':
            #window_content=window_content+'\n\n'
            #print(ori)
            cnt=cnt+1
            ori=insert(ori,'\n',i+window_length)
    print(ori)
    print(cnt)

            
def insert(original,new,position):
    return original[:position] + new + original[position+1:]

binary_chunk('test2_binary.txt')
