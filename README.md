# Deduplicator EC504 Project
## Brief Introduction :
  
  This is the page for **EC504(Spring 2018) Deduplicator project** 
  
  We have five members:
  
  :boy: **Zisen Zhou** jason826@bu.edu   :point_right:[@github/JasonZ82](https://github.com/JasonZ82)
  
  :boy: **Jiaxin Tang** jxtang@bu.edu   :point_right:[@github/jxtang0920](https://github.com/jxtang0920)
  
  :boy: **Ganquan Wen** wengq@bu.edu   :point_right:[@github/GanquanWen](https://github.com/GanquanWen)
  
  :boy: **Xiang Zheng** zhengx95@bu.edu   :point_right:[@github/XiangZheng2017](https://github.com/XiangZheng2017)
  
  :boy: **Zulin Liu** liuzulin@bu.edu   :point_right:[@github/liuzulin](https://github.com/liuzulin)
  
  :mailbox_closed:Please feel free to contact us, if you have any suggestions or concerns. 
  
## Project Description :

:new_moon: The aim :golf: of the project：
       
   * Design and implement an efficient data storage locker that utilizes deduplication.
             
   * Locker should be able to receive files and store them (for later retrieval) with a minimum storage by storing some common data blocks only once.
   
:waxing_crescent_moon: The project is based on    :**Python 3**

:first_quarter_moon: Our project will implement:

   * ASCII and Binary file storage and retrieve.
   
   * Retrieve all files stored in the locker in any order and at any time.
   
   * Graphic User Interface by package tkinter in python
   
   * File deletion without influncing other files.

   


## Algorithm:

#### Variable sized chunking for ASCII and Binary files :
* Fixed-size chunking method splits files into equally sized chunks. As it splits the file into fixed size, byte shifting problem occurs for the altered file. If the bytes are inserted or deleted on the file, it changes all subsequent chunk position which results in duplicate index values. So, fixed-size block chunking has an issue when it comes to finding matching contents in similar files when the content at the beginning of the files is changed. 
  
* So we use variable sized chuncking. For ASCII file, we segment file by paragraph; for Binary file, we use sliding window.
  
#### High-level Diagram:

  https://raw.githubusercontent.com/GanquanWen/Deduplicator/master/Algorithm.PNG

#### Enjoy the code and have fun!:


