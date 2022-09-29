import sys
sys.stdin = open("1_나머지.txt")

result=[]
for i in range(10):
    a = int(input())%42
    result.append(a)
result1 = dict.fromkeys(result)
print(len(result1))
