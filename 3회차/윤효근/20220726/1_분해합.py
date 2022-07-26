import sys

sys.stdin = open("0_최대공약수와 최소공배수.txt")

a=input()
b= map(int,a)
scan = 9*len(list(b))
for i in range(int(a)-scan,int(a)+1):
    result = i + sum(map(int,str(i)))
    if result == int(a):
        print(i)
        break
    if i == int(a):
        print(0)