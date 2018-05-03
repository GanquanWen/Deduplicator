# Deduplicator EC504 Project
## Brief Introduction :
  
  This repository is for **EC504(Spring 2018) Deduplicator project** 
  
  Our team members:
  
   **Zisen Zhou** jason826@bu.edu   :point_right:[@github/JasonZ82](https://github.com/JasonZ82)
  
   **Jiaxin Tang** jxtang@bu.edu   :point_right:[@github/jxtang0920](https://github.com/jxtang0920)
  
   **Ganquan Wen** wengq@bu.edu   :point_right:[@github/GanquanWen](https://github.com/GanquanWen)
  
   **Xiang Zheng** zhengx95@bu.edu   :point_right:[@github/XiangZheng2017](https://github.com/XiangZheng2017)
  
   **Zulin Liu** liuzulin@bu.edu   :point_right:[@github/liuzulin](https://github.com/liuzulin)
  
  If you have any suggestions or concerns, feel free to contact us.
  
## Project Description :

The final program is in folder [***main***](/main), please check the readme in main for details.

Other folders are for each function.

The aim of the project：
       
   * Design and implement an efficient data storage structure that utilizes deduplication.
             
   * Lockers should be able to receive files and store them (for later retrieval) with a minimum storage by storing some common data blocks only once.
   
The project is based on   :**Python 3**

Our project will implement:

   * ASCII and Binary file storage and retrieve.
   
   * Retrieve all files stored in the locker in any order and at any time.
   
   * Graphic User Interface by package tkinter in python
   
   * File deletion without influencing other files.

   


## Algorithm:

#### Variable sized chunking for ASCII and Binary files :
* Fixed-size chunking method splits files into equally sized chunks. As it splits the file into fixed size, byte shifting problem occurs for the altered file. If the bytes are inserted or deleted on the file, it changes all subsequent chunk position which results in duplicate index values. So, fixed-size block chunking has an issue when it comes to finding matching contents in similar files when the content at the beginning of the files is changed. 
  
* So we use variable sized chuncking. For ASCII file, we segment file by paragraph; for Binary file, we use sliding window.
  
#### High-level Diagram:
![image](https://github.com/GanquanWen/Deduplicator/blob/master/Algorithm.PNG)

#### Gui demo:
https://youtu.be/g07wQtD40kI

#### Thanks for coming!


