"""从键盘输入一些字符，逐个把它们写到磁盘文件上，直到输入一个 # 为止"""
filename=("D:\\python_100例\\")
# a=input("请输入字符，#键结束")
# while a !="#":
#     print(a)
exit=False
while not exit:
    s=input("输入字符以#结束")
    if "#" in s:
        n=s.index("#")
        s=s[:n]
        l=l+s
        exit=True

    a=open(filename+"text04","w")
    a.write(s)


