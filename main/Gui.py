from tkinter import *
from tkinter import messagebox
import time
from tkinter import ttk
import threading
from tkinter import filedialog
import hashlib
import os
import re
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
def ASCII_chunk(filename, dic, path):
    '''
    read from file
    create and renew the dictionary
    write chunks to file in current path
    '''
    article_hash_lst = []
    with open(filename, 'r') as myfile:
        data = myfile.read()
    tmp = re.split(r"(\n\n)", data)
    tmp.append("")
    tmp = ["".join(i) for i in zip(tmp[0::2],tmp[1::2])]
    length = len(tmp)
    if length < 1000:
            step = 1
    else:
        step = length//1000
    rng = length // 10
    list_rng=[rng*i for i in range(11)]
    t = 0
    for i in range(0,length,step):
        tmp2 = ''
        if i + step < length:
            for j in range(i,i + step):
                tmp2 += tmp[j]
        else:
            for j in range(i,length):
                tmp2 += tmp[j]
        hashstr = tmp2.encode('utf-8')
        hashtmp = para_hash(hashstr)
        article_hash_lst.append(hashtmp)
        if hashtmp in dic:
            if os.path.basename(filename) not in dic[hashtmp]:
                dic[hashtmp].append(os.path.basename(filename))
        else:
            chunkname = path + hashtmp + ('.txt')
            dic[hashtmp] = [os.path.basename(filename)]
            text_file = open(chunkname, "w")
            text_file.write(tmp2)
            text_file.close()
        if i > list_rng[t]:
            t += 1
            app.progressbar["value"] = i
            app.progressbar["maximum"] = list_rng[-2]
            app.change_schedule(i,list_rng[-2]) 
    #create artile list file
    article_hash_lst_filename = path+'list_'+os.path.basename(filename)
    article_hash_lst_file=open(article_hash_lst_filename,'w')
    article_hash_lst_file.write(str(article_hash_lst).strip('[').strip(']'))
    return article_hash_lst

def timeinterval(size):
    if size<10000000:
        return 3
    elif size<100000000:
        return 10
    else:
        return 100

def binary_chunk(filename,dic,path):
    with open(filename, 'r') as myfile:
        s = myfile.read()
    size = len(s)
    tt = timeinterval(size)
    rng = size//tt
    list_rng=[rng*i for i in range(tt+1)]
    article_hash_lst = []
    if size < 100000:
        window_length = size // 100
        pattern = '101'
    else:    
        window_length = size // 1000
        pattern = '010101'
    step = 1
    flag = 0 
    i = 0
    j = 0
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
            if i > list_rng[j]:
                j += 1
                app.progressbar["value"] = i
                app.progressbar["maximum"] = list_rng[-2]
                app.change_schedule(i,list_rng[-2]) 
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
        line = f.readline()
    f.close()
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
    f = open(file, "r")
    line = f.readline()
    f.close()
    org_list = line.split(", ")
    parts_list = []
    for n in range(len(org_list)):
        parts_list.append(org_list[n].strip("\'"))
    '''retrieve each part of the original article by the hash
       connect them to make a string'''
    #
    size = len(parts_list)
    tt = timeinterval(size)
    rng = size//tt
    list_rng=[rng*i for i in range(tt+1)]
    fre=0
    j=0
    #
    original_file = ""
    for i in range(len(parts_list)):
        part_file = open(path+parts_list[i]+'.txt', "r")
        line = part_file.readline()
        while line:
            original_file += line
            line = part_file.readline()
        # if i < len(parts_list)-1:
        #     original_file += '\n\n'  # adding a blank line between each part
        part_file.close()
        fre+=1
        if fre >=list_rng[j]:
            j+=1
            app.progressbar["value"] = fre
            app.progressbar["maximum"] = list_rng[-2]
            app.change_schedule(fre,list_rng[-2])
    '''store the article as txt file'''
    file_name_split = file.split('/')
    file_name = file_name_split[-1].lstrip('list_')
    file_name = file_name.rstrip('.txt')
    output_file = open(file_name+'_retrieved.txt', "w")
    output_file.write(original_file)
    output_file.close()
    return original_file

def bi_retrieve(file, path):
    '''get the list of hash
       then retrieve the file according to hash in order
    '''
    f = open(file, "r")
    line = f.readline()
    f.close()
    org_list = line.split(", ")
    parts_list = []
    for n in range(len(org_list)):
        parts_list.append(org_list[n].strip("\'"))
    '''retrieve each part of the original article by the hash
       connect them to make a string'''
    #
    size = len(parts_list)
    tt = timeinterval(size)
    rng = size//tt
    list_rng=[rng*i for i in range(tt+1)]
    fre=0
    j=0
    #
    original_file = ""
    for i in range(len(parts_list)):
        part_file = open(path+parts_list[i]+'.txt', "r")
        line = part_file.readline()
        while line:
            original_file += line
            line = part_file.readline()
        part_file.close()
        fre+=1
        if fre >=list_rng[j]:
            j+=1
            app.progressbar["value"] = fre
            app.progressbar["maximum"] = list_rng[-2]
            app.change_schedule(fre,list_rng[-2])

    '''store the article as txt file'''
    file_name_split = file.split('/')
    file_name = file_name_split[-1].lstrip('list_')
    file_name = file_name.rstrip('.txt')
    output_file = open(file_name+'_retrieved.txt', "w")
    output_file.write(original_file)
    output_file.close()
    return original_file

def delete(file, path):
    '''get the list of hash
       then delete every part on the list according to hash in order
    '''
    M = get_iven('Inventory.txt','')
    f = open(file, "r")
    line = f.readline()
    f.close()
    file_name_split = file.split('/')
    file_name = file_name_split[-1].lstrip('list_')
    org_list = line.split(", ")
    parts_list = []
    for n in range(len(org_list)):
        parts_list.append(org_list[n].strip("\'"))
    #
    size = len(parts_list)
    tt = timeinterval(size)
    rng = size//tt
    list_rng=[rng*i for i in range(tt+1)]
    fre=0
    j=0
    #
    for part in parts_list:
        if part in M:
            if len(M[part]) == 1:
                os.remove(path+part+'.txt')
                print('remove '+path+part+'.txt')
                del M[part]
            else:
                if file_name in M[part]:
                    M[part].remove(file_name)
        else:
            continue
        fre+=1
        if fre >=list_rng[j]:
            j+=1
            app.progressbar["value"] = fre
            app.progressbar["maximum"] = list_rng[-2]
            app.change_schedule(fre,list_rng[-2]) 
    os.remove(file)
    print (file + ' deleted')
    dic = M
    Inven_dic=open('Inventory.txt','w')
    for key in dic:
        info="{} ".format(key)
        Inven_dic.write(str(info))
        for child in range(0,len(dic[key])):
            info="{} ".format(dic[key][child])
            Inven_dic.write(str(info))
        Inven_dic.write('\n')
    return M

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
        self.insertButton = Button(self, text='Store ASCII File', command=self.insert_Button)
        self.insertButton.grid(row = 5,column = 0)
        self.insertBFileButton = Button(self, text='Store Binary File', command=self.insert_Binary_Button)
        self.insertBFileButton.grid(row = 5,column = 1)
        self.retrieveAButton = Button(self, text='Retrieve ACSCII File', command=self.retrieve_Button)
        self.retrieveAButton.grid(row = 6,column = 0)
        self.retrieveBButton = Button(self, text='Retrieve Binary FIle', command=self.retrieve_Binary_Button)
        self.retrieveBButton.grid(row = 6,column = 1)
        self.deleteButton = Button(self, text='Delete', command=self.delete_Button)
        self.deleteButton.grid(row = 7,column = 0)
        self.quitButton = Button(self, text="QUIT", fg="red", command=self.quit)
        self.quitButton.grid(row = 7,column = 1)
        self.progressbar = ttk.Progressbar(self, orient="horizontal", length=200, mode="determinate")
        self.progressbar.grid(row=8, column=0)
    #Function to refresh Progressbar
    def choose_File(self):
        filename = filedialog.askopenfilename(title = "Select File",filetypes = (("text file","*.txt"),("","")))
        self.nameInput['state'] = 'normal'
        self.nameInput.delete(0,'end')
        self.nameInput.insert(0,str(filename))
        self.nameInput['state'] = 'disable'
    def choose_AFile(self):
        filename = filedialog.askopenfilename(title = "Select File",filetypes = (("text file","*.txt"),("","")))
        self.nameInput['state'] = 'normal'
        self.nameInput.delete(0,'end')
        self.nameInput.insert(0,str(filename))
        self.nameInput['state'] = 'disable'
    def choose_Locker(self):
        lockername = filedialog.askdirectory(title = "Select Folder")
        self.lockerInput['state'] = 'normal'
        self.lockerInput.delete(0,'end')
        self.lockerInput.insert(0,str(lockername))
        self.lockerInput['state'] = 'disable'
    def change_schedule(self,now_schedule,all_schedule):
        x=StringVar()
        self.canvasLabel = Label(self,textvariable = x)
        self.canvasLabel.grid(row = 8,column = 1)
        self.update()
        x.set(str(round(now_schedule/all_schedule*100,0)) + '%')  
        if now_schedule>=all_schedule:
            app.progressbar.stop()
            x.set("Finish")
            self.canvasLabel['font']=30
    def disable_buttons(self):
        self.fileButton.configure(state = 'disable')
        self.lockerButton.configure(state = 'disable')
        self.insertButton.configure(state = 'disable')
        self.insertBFileButton.configure(state = 'disable')
        self.deleteButton.configure(state = 'disable')
        self.retrieveAButton.configure(state = 'disable')
        self.retrieveBButton.configure(state = 'disable')
        self.quitButton.configure(state = 'disable')
    def enable_buttons(self):
        self.fileButton.configure(state = 'normal')
        self.lockerButton.configure(state = 'normal')
        self.insertButton.configure(state = 'normal')
        self.insertBFileButton.configure(state = 'normal')
        self.deleteButton.configure(state = 'normal')
        self.retrieveAButton.configure(state = 'normal')
        self.retrieveBButton.configure(state = 'normal')
        self.quitButton.configure(state = 'normal')
    #insert binary file
    def insert_Binary_Button(self):
        name = self.nameInput.get() or messagebox.showerror("Error", "Please select the File")
        if name !=self.nameInput.get():
            return 0
        locker= self.lockerInput.get() or messagebox.showerror("Error", "Please select the Locker")
        if locker !=self.lockerInput.get():
            return 0
        starttime=time.time()
        self.progressbar.start()
        self.disable_buttons()
        try:
            insertbinary(name,locker+'/')
        except:
            messagebox.showerror("Error","Please select the correct file and path")
            self.progressbar.stop()
            self.enable_buttons()
            return 0
        # insertbinary(name,locker+'/')
        self.progressbar.stop()
        endtime=time.time()
        totaltime = endtime - starttime
        messagebox.showinfo('Message', 'Store file '+ name + ' to locker '+ locker +'\nTotal time is '+ str(totaltime))
        self.enable_buttons()

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
        self.disable_buttons()
        try:
            insertASCII(name,locker+'/')
        except:
            messagebox.showerror("Error","Please select the correct file and path")
            self.progressbar.stop()
            self.enable_buttons()
            return 0
        # insertASCII(name,locker+'/')
        self.progressbar.start()
        self.progressbar.stop()
        endtime=time.time()
        totaltime = endtime - starttime
        messagebox.showinfo('Message', 'Store file '+ name + ' to locker '+ locker +'\nTotal time is '+ str(totaltime))
        self.enable_buttons()
    
    #Delete Function
    def delete_Button(self):
        name = self.nameInput.get() or messagebox.showerror("Error", "Please select the File")
        if name !=self.nameInput.get():
            return 0
        locker= self.lockerInput.get() or messagebox.showerror("Error", "Please select the Locker")
        if locker !=self.lockerInput.get():
            return 0
        filename = name.split('/')
        if 'list' not in filename[-1]:
            messagebox.showerror("Error","Please select the list file for delete")
            return 0
        starttime = time.time()
        self.progressbar.start()
        self.disable_buttons()
        try:
            delete(name,locker+'/')
        except:
            messagebox.showerror("Error","Please select the correct file and path")
            self.progressbar.stop()
            self.enable_buttons()
            return 0
        # delete(name,locker+'/')
        self.progressbar.stop()
        endtime = time.time()
        totaltime = endtime - starttime
        messagebox.showinfo('Message', 'Delete file '+ name +' from locker '+ locker+'\nTotal time is '+ str(totaltime) )
        self.enable_buttons()

    #Retrieve Function
    def retrieve_Button(self):
        name = self.nameInput.get() or messagebox.showerror("Error", "Please Select the File")
        if name !=self.nameInput.get():
            return 0
        locker= self.lockerInput.get() or messagebox.showerror("Error", "Please select the Locker")
        if locker !=self.lockerInput.get():
            return 0
        filename = name.split('/')
        if 'list' not in filename[-1]:
            messagebox.showerror("Error","Please select the list file for retrieve")
            return 0
        starttime=time.time()
        self.progressbar.start()
        self.disable_buttons()
        try:
            retrieve(name,locker+'/')
        except:
            messagebox.showerror("Error","Please select the correct file and path")
            self.progressbar.stop()
            self.enable_buttons()
            return 0
        self.progressbar.stop()
        endtime=time.time()
        totaltime = endtime-starttime
        messagebox.showinfo('Message','Retrieve file ' + name+ ' from locker '+ locker +'\nTotal time is '+ str(totaltime) )
        self.enable_buttons()

    def retrieve_Binary_Button(self):
        name = self.nameInput.get() or messagebox.showerror("Error", "Please Select the File")
        if name !=self.nameInput.get():
            return 0
        locker= self.lockerInput.get() or messagebox.showerror("Error", "Please select the Locker")
        if locker !=self.lockerInput.get():
            return 0
        filename = name.split('/')
        if 'list' not in filename[-1]:
            messagebox.showerror("Error","Please select the list file for retrieve")
            return 0
        starttime=time.time()
        self.progressbar.start()
        self.disable_buttons()
        try:
            bi_retrieve(name,locker+'/')
        except:
            messagebox.showerror("Error","Please select the correct file and path")
            self.progressbar.stop()
            self.enable_buttons()
            return 0
        self.progressbar.stop()
        endtime=time.time()
        totaltime = endtime-starttime
        messagebox.showinfo('Message','Retrieve file ' + name+ ' from locker '+ locker +'\nTotal time is '+ str(totaltime) )
        self.enable_buttons()


def insertbinary(filename,locker):
    # filename = 'main/sample_binary/file1.txt'
    with open(filename, 'r') as myfile:
        data = myfile.read()
    inv = 'Inventory.txt'
    try:
        dic = get_iven('Inventory.txt','')
    except:
        dic = {}
    binary_chunk(filename,dic,locker)
    Inven_dic=open(inv,'w')
    for key in dic:
        info="{} ".format(key)
        Inven_dic.write(str(info))
        for child in range(0,len(dic[key])):
            info="{} ".format(dic[key][child])
            Inven_dic.write(str(info))
        Inven_dic.write('\n')

def insertASCII(filename,locker):
    # filename = 'main/sample_ASCII/file1.txt'
    with open(filename, 'r') as myfile:
        data = myfile.read()
    inv = 'Inventory.txt'
    try:
        dic = get_iven('Inventory.txt','')
    except:
        dic = {}
    ASCII_chunk(filename,dic,locker)
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