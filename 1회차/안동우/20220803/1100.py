from pprint import pprint
import sys
sys.stdin = open("1100.txt", "r")

a=[]
for i in range(8):
    b=list(input())
    a.append(b)
c=0# F수
for i in range(8):
    for k in range(8):
        if (i+k)%2 == 0 and a[i][k]=='F':
            c+=1# F수
print(c)