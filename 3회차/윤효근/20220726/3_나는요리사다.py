
import sys

sys.stdin = open("0_최대공약수와 최소공배수.txt")

result =[]
for i in range(5):
    b= list(map(int,input().split()))
    result.append(sum(list(b)))

print(result.index(max(result))+1)
print(max(result))