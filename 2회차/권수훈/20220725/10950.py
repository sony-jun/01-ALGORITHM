from re import A


numberOfTimes = int(input())

for i in range(1,numberOfTimes+1):
    a,b = map(int,input().split())
    print(a+b)