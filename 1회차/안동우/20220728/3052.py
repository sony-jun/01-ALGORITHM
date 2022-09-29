import sys
sys.stdin = open("3052.txt", "r")

a=[]
for i in range(10):
    b=int(input())
    a.append(b%42)
a=set(a)
print(len(a))