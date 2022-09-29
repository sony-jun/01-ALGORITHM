# https://www.acmicpc.net/problem/8958
import sys

sys.stdin = open("3_OX퀴즈.txt")


T = int(sys.stdin.readline())

for i in range(1,T+1):
    sum_list=[]
    check_list=[]
    a = list(sys.stdin.readline())
    
    for k in range(0,len(a)):
        if a[k] == 'O':
            check_list.append(1)
        else:
            check_list.append(0)

    for l in range(1, len(check_list)):
        if a[l-1] == 'O' and a[l] == 'O':
            check_list[l] += check_list[l-1]
    print(sum(check_list))
