"""输入一个奇数，然后判断最少几个 9 除于该数的结果为整数"""
a=int(input("请输入一个奇数："))
b=0

for i in range(0,99):
    b+=9*10**i
    if b%a==0:
        print("奇数%d最少有%d个9整除 %d/%d=%d"%(a,i+1,b,a,b/a))
        break

