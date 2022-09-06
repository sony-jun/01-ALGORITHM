import sys
from unittest import result


sys.stdin = open('1292.txt')
result=[]
a , b = map(int , input().split())

for i in range(1 , b+1):
    for y in range(i):
        result.append(i)
print(result[a - 1:b])
