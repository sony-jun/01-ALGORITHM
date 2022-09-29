# 관찰 기록을 가지고 소가 최소 몇 번 길을 건넜는지 알아보자.

dict = {}
l=[]
n=int(input())
for i in range(n):
    loc = list(map(int,input().split()))
    l.append(loc)
    dict[l[0]]=l[1]
print(l)
print(dict)