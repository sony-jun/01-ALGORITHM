
import sys

sys.stdin = open("3_나는요리사다.txt")


result =[]
for i in range(5):
    b= list(map(int,input().split()))
    result.append(sum(list(b)))

print(result.index(max(result))+1)
print(max(result))