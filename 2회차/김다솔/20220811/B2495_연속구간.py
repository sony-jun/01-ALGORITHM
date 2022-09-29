# https://www.acmicpc.net/problem/2495
import sys
sys.stdin = open('B2495.txt')

for _ in range(6):  # 여덟자리 정수 3개
    num = int(input())
    num_list= list(map(int, str(num))) #한자리씩 리스트로 변경
    series_len = []
    cnt = 1
    # print(num)
    for i in range(len(num_list)-1):        
        if num_list[i] == num_list[i + 1]:
            cnt += 1
        else: 
            series_len.append(cnt)
            cnt = 1
            continue
    series_len.append(cnt)
    print(max(series_len))
            