import unittest
from subprocess import call
import sys
import delete
import insert
import fileretrieve
call(["mkdir","Locker"])
insert.insertASCII("sample_ASCII/file1.txt","Locker/")
insert.insertASCII("sample_ASCII/file2.txt","Locker/")
fileretrieve.retrieve("file1.txt","Locker/")
f1 = open("sample_ASCII/file1.txt",'r')
f2 = open("file1_retrieved.txt","r")
f1content = f1.read()
f2content = f2.read()
print(f1content[1:100])
print("****************")
print(f2content[1:100])
if f1content == f2content:
	print("yes")
else:
	print("no")
delete.delete("file2.txt","Locker/")
