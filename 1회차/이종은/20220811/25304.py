import sys 
sys.stdin = open('input.txt')

n = int(input())
m = int(input())

list_ = []
for _ in range(m):
    a, b = map(int, input().split())
    list_.append(a*b)

if sum(list_) == n:
    print("Yes")
else:
    print("No")

print(sum(list_))