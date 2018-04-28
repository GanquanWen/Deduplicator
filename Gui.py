from tkinter import *
from tkinter import messagebox
import time
from tkinter import ttk
import threading
from tkinter import filedialog
import hashlib
import os
#import tkMessageBox
#Test function for progress bar
# def start(rangeValue):
#     for i in range(rangeValue+1):  
#         time.sleep(0.1)
#         app.change_schedule(i,rangeValue)
        # app.progressbar["value"] = i
        # app.progressbar["maximum"] = rangeValue

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
        app.progressbar["value"] = i
        app.progressbar["maximum"] = length
        app.change_schedule(i,length)
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
        app.progressbar["value"] = i
        app.progressbar["maximum"] = len(s)
        app.change_schedule(i,len(s))
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
        # print(parts_list[i])
        inventory[parts_list[i][0]] = []
        for k in range(1, len(parts_list[i])):
            inventory[parts_list[i][0]].append(parts_list[i][k])
    return inventory

def retrieve(file, path):
    '''get the list of hash
       then retrieve the file according to hash in order
    '''
    f = open(path+file, "r")
    line = f.readline()
    f.close()
    org_list = line.split(", ")
    parts_list = []
    for n in range(len(org_list)):
        parts_list.append(org_list[n].strip("\'"))
    print(parts_list)
    '''retrieve each part of the original article by the hash
       connect them to make a string'''
    original_file = ""
    for i in range(len(parts_list)):
        part_file = open(path+parts_list[i]+'.txt', "r")
        line = part_file.readline()
        while line:
            original_file += line
            line = part_file.readline()
        if i < len(parts_list)-1:
            original_file += '\n\n'  # adding a blank line between each part
        part_file.close()
        app.progressbar["value"] = i
        app.progressbar["maximum"] = len(parts_list)
        app.change_schedule(i,len(parts_list))
    '''store the article as txt file'''
    file_name = file.lstrip('list_')
    output_file = open(path + file_name, "w")
    output_file.write(original_file)
    output_file.close()
    return original_file
       
# def insert(original,new,position):
#     return original[:position] + new + original[position:]

class Application(Frame):
    #Initial function
    def __init__(self,master=None):
        Frame.__init__(self, master)
        self.pack()
        self.createWidgets()
        self.thread = threading.Thread()
        self.thread.start()
    #Function to add all widgets
    def createWidgets(self):
        self.helloLabel = Label(self, text='Welcom to our Locker system!')
        self.helloLabel.grid(row = 0,column = 0)
        self.fileLabel = Label(self, text='Please select the File')
        self.fileLabel.grid(row = 1,column = 0)
        self.nameInput = Entry(self,width = 30,state='disable')
        self.nameInput.grid(row = 1,column = 1)
        self.lockerLabel = Label(self, text='Please select the Locker')
        self.lockerLabel.grid(row = 3,column = 0)
        self.lockerInput = Entry(self,width = 30,state='disable')
        self.lockerInput.grid(row = 3,column = 1)
        self.fileButton = Button(self, text='Select File',command = self.choose_File)
        self.fileButton.grid(row = 2, column = 0)
        self.lockerButton = Button(self, text='Select Locker',command = self.choose_Locker)
        self.lockerButton.grid(row = 4, column = 0)
        self.insertButton = Button(self, text='Insert', command=self.insert_Button)
        self.insertButton.grid(row = 5,column = 0)
        self.deleteButton = Button(self, text='Delete', command=self.delete_Button)
        self.deleteButton.grid(row = 6,column = 0)
        self.retrieveButton = Button(self, text='Retrieve', command=self.retrieve_Button)
        self.retrieveButton.grid(row = 7,column = 0)
        self.quitButton = Button(self, text="QUIT", fg="red", command=self.quit)
        self.quitButton.grid(row = 6,column = 1)
        self.progressbar = ttk.Progressbar(self, orient="horizontal", length=200, mode="determinate")
        self.progressbar.grid(row=8, column=0)
        # self.canvas = Canvas(self,width = 120,height = 30,bg = "white")
        # self.canvas.grid(row = 10,column = 0)
        # self.thread = threading.Thread()
        # self.thread.__init__(target=self.progressbar.start(self.interval),args=())
        # self.thread.start()
    #Function to refresh Progressbar
    def choose_File(self):
        filename = filedialog.askopenfilename(title = "Select File",filetypes = (("text file","*.txt"),("","")))
        self.nameInput['state'] = 'normal'
        self.nameInput.insert(0,str(filename))
        self.nameInput['state'] = 'disable'
    def choose_Locker(self):
        lockername = filedialog.askdirectory(title = "Select Folder")
        self.lockerInput['state'] = 'normal'
        self.lockerInput.insert(0,str(lockername))
        self.lockerInput['state'] = 'disable'

    def change_schedule(self,now_schedule,all_schedule):
        x=StringVar()
        self.canvasLabel = Label(self,textvariable = x)
        self.canvasLabel.grid(row = 8,column = 1)
        # out_rec=self.canvas.create_rectangle(5,5,105,25,outline = "blue",width = 1)
        # fill_rec=self.canvas.create_rectangle(5,5,5,25,outline = "",width = 0,fill = "blue")
        # self.canvas.coords(fill_rec, (5, 5, 6 + (now_schedule/all_schedule)*100, 25))   
        self.update()
        x.set(str(round(now_schedule/all_schedule*100,2)) + '%')  
        if round(now_schedule/all_schedule*100,2) == 100.00:
            x.set("Finish")
    
    #Insert Function
    def insert_Button(self):
        name = self.nameInput.get() or messagebox.showerror("Error", "Please select the File")
        if name !=self.nameInput.get():
            return 0
        locker= self.lockerInput.get() or messagebox.showerror("Error", "Please select the Locker")
        if locker !=self.lockerInput.get():
            return 0
        starttime=time.time()
        self.progressbar.start()
        self.insertButton.configure(state = 'disable')
        self.deleteButton.configure(state = 'disable')
        self.retrieveButton.configure(state = 'disable')
        self.quitButton.configure(state = 'disable')
        insertFile()
        self.progressbar.stop()
        endtime=time.time()
        totaltime = endtime - starttime
        messagebox.showinfo('Message', 'Insert file '+ name + ' to locker '+ locker +'\nTotal time is '+ str(totaltime))
        self.insertButton.configure(state = 'normal')
        self.deleteButton.configure(state = 'normal')
        self.retrieveButton.configure(state = 'normal')
        self.quitButton.configure(state = 'normal')
    
    #Delete Function
    def delete_Button(self):
        name = self.nameInput.get() or messagebox.showerror("Error", "Please select the File")
        if name !=self.nameInput.get():
            return 0
        locker= self.lockerInput.get() or messagebox.showerror("Error", "Please select the Locker")
        if locker !=self.lockerInput.get():
            return 0
        starttime = time.time()
        self.progressbar.start()
        self.insertButton.configure(state = 'disable')
        self.deleteButton.configure(state = 'disable')
        self.retrieveButton.configure(state = 'disable')
        self.quitButton.configure(state = 'disable')
        #操作一下
        self.progressbar.stop()
        endtime = time.time()
        totaltime = endtime - starttime
        messagebox.showinfo('Message', 'Delete file '+ name +' from locker '+ locker+'\nTotal time is '+ str(totaltime) )
        self.insertButton.configure(state = 'normal')
        self.deleteButton.configure(state = 'normal')
        self.retrieveButton.configure(state = 'normal')
        self.quitButton.configure(state = 'normal')

    #Retrieve Function
    def retrieve_Button(self):
        name = self.nameInput.get() or messagebox.showerror("Error", "Please Select the File")
        if name !=self.nameInput.get():
            return 0
        locker= self.lockerInput.get() or messagebox.showerror("Error", "Please select the Locker")
        if locker !=self.lockerInput.get():
            return 0
        starttime=time.time()
        self.progressbar.start()
        self.insertButton.configure(state = 'disable')
        self.deleteButton.configure(state = 'disable')
        self.retrieveButton.configure(state = 'disable')
        self.quitButton.configure(state = 'disable')
        file = 'list_org_file_a.txt'
        path = 'retrieve/test/'
        retrieve(file, path)
        self.progressbar.stop()
        endtime=time.time()
        totaltime = endtime-starttime
        messagebox.showinfo('Message','Retrieve file ' + name+ ' from locker '+ locker +'\nTotal time is '+ str(totaltime) )
        self.insertButton.configure(state = 'normal')
        self.deleteButton.configure(state = 'normal')
        self.retrieveButton.configure(state = 'normal')
        self.quitButton.configure(state = 'normal')

def insertFile():
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


app = Application()
def main():
    dic={}
    app.master.title('Deduplicator')
    app.master.maxsize(1000,1000)
    app.master.minsize(500,300)
    app.mainloop()



if __name__ == '__main__':
    main()
