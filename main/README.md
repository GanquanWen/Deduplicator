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
