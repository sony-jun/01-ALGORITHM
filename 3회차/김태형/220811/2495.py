# 같은 숫자가 연속해서 나오는 구간 중 가장 긴 것의 길이를 출력하는 프로그램을 작성하라. 

import sys
sys.stdin = open("2495.txt")

for i in range(3):
    l = input()
    s = set(l)
    dict = {}
    # 딕셔너리를 통한 풀이
    for i in s:
        dict[i]=0
    for i in dict:
        for j in range(len(l)):
            if i==l[j] and l[j-1]==l[j]:
                dict[i]+=1
            else:
                continue
    print(dict)
