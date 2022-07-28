import sys
sys.stdin = open("20220728/3052_나머지.txt")

num = []

for i in range(10):
    num.append(int(input())%42)

count = len(set(num))
print(count)