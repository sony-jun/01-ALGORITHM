# https://www.acmicpc.net/problem/1292

import sys
sys.stdin = open("/Users/yuyeong/Desktop/알고리즘/01-ALGORITHM/1회차/김유영/20220728/16_쉽게 푸는 문제.txt")


# A, B를  입력 받고 0에서 B까지 반복
A, B = map(int, input().split())
arr = []
for i in range(1, B+1):
    # i 만큼 반복해서 리스트 arr에 넣어줌
    for j in range(i):
        arr.append(i)
print(arr[A-1:B])
# print(sum(arr[A-1:B]))
