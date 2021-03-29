"""某个公司采用公用电话传递数据，数据是四位的整数，在传递过程中是加密的，
加密规则如下：每位数字都加上5,然后用和除以10的余数代替该数字，再将第一位和第四位交换，第二位和第三位交换"""

a=input("连续输入四个数字：")
l=[]
for i in range(4):
    b=int(a[i])+5
    c=b%10
    l.append(c)
    l.reverse()

    # l.insert(0,c)
    # print(c)

print("".join("%s" %i for i in l))
