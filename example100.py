"""题目：列表转换为字典。"""

# 解题，dict()通过映射函数构造字典
l1=[1,2,3]
l2=["a","b","c"]
dic1=dict(zip(l1,l2))
print(dic1,type(dic1))


# dict()通过传入关键字构造字典
dict2=dict(a1='a', b1='b', t1='t')
print(dict2,type(dict2))

# dict()传入可迭代对象构造字典
dict3=dict([('one', 1), ('two', 2), ('three', 3)])
print(dict3,type(dict3))

