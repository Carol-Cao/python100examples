"""从键盘输入一个字符串，将小写字母全部转换成大写字母，然后输出到一个磁盘文件"test"中保存。"""
from sys import stdout
path=("D:\\python_100例\\")

a=input("请输入小写字母")
b=a.upper()
c=open(path+"test.txt","w")
c.write(b)
c.close()
# print(a,b)
