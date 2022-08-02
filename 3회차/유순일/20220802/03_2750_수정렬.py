import sys

sys.stdin = open("2750.txt", "r")

N = int(input())

list_ = []
for tc in range(1, N + 1):
    list_.append(int(input()))
    
    list_1 = sorted(list_)

for i in range(len(list_1)):
    print(list_1[i])