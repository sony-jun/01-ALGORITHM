# 어떤 글이 주어졌을 때, 가장 많이 나온 글자를 출력하는 프로그램을 작성하시오.
import sys

s = sys.stdin.read()
set_s = set(s)
dict={}
for i in set_s:
    dict[i]=0
for i in dict:
    dict[i]+=s.count(i)
max_dict = max(dict.values())
for i in dict:
    if dict[i]==max_dict:
        print(i,end='')