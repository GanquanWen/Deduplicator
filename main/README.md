# 
[Command line User](#Title2)
# How to use Command Line User Interface

### 1. Run clui.py with Python3.6

```
$ python clui.py
```

### 2. Store file in locker

The folder 'locker' needs to be existed. You can create a folder for this.

The file will be splited into parts and stored in locker. A inventory file (Inventory.txt) will be created in the same folder with the clui.py. Also, a list of all the parts that the file has will be store as list_filename.txt in locker.

The inventory is essential for storing and deleting. And the list is for deleting and retrieving the corresponding file.

You can use one of the sample file in folder 'sample_ASCII' or 'sample_binary'
(storea for ACSII file, storeb for binary file)
Pay attention: the '/' behind the folder name is necessary. And the path is start at the main folder. If you want to get to other folder, it should start with "./"

```
storea -file file1.txt -path locker/
storea -file sample_ASCII/file2.txt -path locker/
storeb -file sample_binary/file3.txt -path locker/
```

### 3. Retrieve file

The retrieved file will be saved in the root folder of clui.py.

```
retrieve -file file1.txt -path locker/
retrieve -file file2.txt -path locker/
```

### 4. Delete file

After deleting the file, the list of the file will be removed. The parts that only be used by the file will be removed from locker. And the inventory will be updated.

```
delete -file file1.txt -path locker/
delete -file file2.txt -path locker/
```

### 5. Exit

Input 'exit' to stop the program.

```
exit
```

# Video Demo of Command Line User Interface

* (https://youtu.be/R8zm1WjIiHk)

# How to use Graphical User Interface

### 1. Run GUi.py with Python3.6

```
$ python Gui.py
```
![image](https://github.com/GanquanWen/Deduplicator/blob/master/picture/store/GUI%20Interface.png)

### 2. Store file in locker

The folder 'locker' needs to be existed. You can create a folder for this.
![image](https://github.com/GanquanWen/Deduplicator/blob/master/picture/store/create%20a%20locker.png)
The file will be splited into parts and stored in locker. A inventory file (Inventory.txt) will be created in the same folder with the clui.py. Also, a list of all the parts that the file has will be store as list_filename.txt in locker.

The inventory is essential for storing and deleting. And the list is for deleting and retrieving the corresponding file.

You can use one of the sample file in folder 'sample_ASCII' or 'sample_binary'.

#### 1. To store the file, first press select file button to select the file you want to store in the locker.
![image](https://github.com/GanquanWen/Deduplicator/blob/master/picture/store/select%20file.png)

#### 2. Then select the locker (floder) that you want to save the file.
![image](https://github.com/GanquanWen/Deduplicator/blob/master/picture/store/select%20locer.png)

#### 3. Click the button with the corresponding type.
![image](https://github.com/GanquanWen/Deduplicator/blob/master/picture/store/select%20button.png)

#### 4. Result
![image](https://github.com/GanquanWen/Deduplicator/blob/master/picture/store/Get%20result.png)

### 3. Retrieve file


#### 1. To retrieve the file, first press select file button to select the list file list_filename in the locker.
![image](https://github.com/GanquanWen/Deduplicator/blob/master/picture/retrieve/Screen%20Shot%202018-05-03%20at%202.22.56%20PM.png)
#### 2. Then select the locker (floder) that the file is saved.
![image](https://github.com/GanquanWen/Deduplicator/blob/master/picture/retrieve/Screen%20Shot%202018-05-03%20at%202.35.18%20PM.png)
#### 3. Click the button with the corresponding type.
![image](https://github.com/GanquanWen/Deduplicator/blob/master/picture/retrieve/Screen%20Shot%202018-05-03%20at%202.44.19%20PM.png)
#### 4. Result
The retrieved file will be saved in the root folder of Gui.py.
![image](https://github.com/GanquanWen/Deduplicator/blob/master/picture/retrieve/Screen%20Shot%202018-05-03%20at%202.49.07%20PM.png)

### 4. Delete file

#### 1. To delete the file, first press select file button to select the list file list_filename in the locker.
![image](https://github.com/GanquanWen/Deduplicator/blob/master/picture/Delete/Screen%20Shot%202018-05-03%20at%203.01.01%20PM.png)
#### 2. Then select the locker (floder) that the file is saved.
![image](https://github.com/GanquanWen/Deduplicator/blob/master/picture/Delete/Screen%20Shot%202018-05-03%20at%203.07.29%20PM.png)
#### 3. Click the button to delete the file.
![image](https://github.com/GanquanWen/Deduplicator/blob/master/picture/Delete/Screen%20Shot%202018-05-03%20at%203.20.38%20PM.png)
#### 4. Result
After deleting the file, the list of the file will be removed. The parts that only be used by the file will be removed from locker. And the inventory will be updated.
![image](https://github.com/GanquanWen/Deduplicator/blob/master/picture/Delete/Screen%20Shot%202018-05-03%20at%203.25.26%20PM.png)


### 5. Exit

Click Quit button to exit the program.

# Video Demo of Graphical User Interface

* (https://youtu.be/g07wQtD40kI)
