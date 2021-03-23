import string
path="D:\\python_100例\\"
fp1,fp2=open(path+"text01.txt"),open(path+"text02.txt")
a,b=fp1.read(),fp2.read()



fp3=open(path+"text03.txt","w")
l=list(a+b)
l.sort()
s=''
s=s.join(l)
fp3.write(s)
fp3.close()
fp2.close()
fp1.close()