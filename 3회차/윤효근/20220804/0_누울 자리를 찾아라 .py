import sys

sys.stdin = open("0_누울 자리를 찾아라 .txt")
n,n1 = map(int,input().split())
a=set(map(int,input().split()))
b=set(map(int,input().split()))

print(len(a^b))
