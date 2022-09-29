import sys
sys.stdin = open("4_수정렬하기.txt")

N = int(input())
list_ =[]

for tc in range(1, N+1):
    x = int(input())
    list_.append(x)

sort_num = sorted(list_)

for i in sort_num:
    print(i)