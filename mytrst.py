# -*- coding: utf-8 -*-
# @Time    : 2020/10/21 7:41 下午
# @Author  : Chaorn Wang
# @Email   : chaoran.wcr@dtwave-inc.com
# @File    : mytrst.py


def numb(s):
 result={}
 for i in s:
    if i in result.keys():
        result[i]=result[i]+1
    else:
        result[i]=1
 return result
fu = input("Please input a new string")
f = numb(fu)
n = list(f.values())
n.sort()
print(n)
print(n[-2])
i = n[-2]
for item in f.keys():
  if i == f[item]:
    print(item)