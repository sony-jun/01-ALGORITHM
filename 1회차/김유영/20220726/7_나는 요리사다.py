# https://www.acmicpc.net/problem/2953

import sys
sys.stdin = open("/Users/yuyeong/Desktop/알고리즘/01-ALGORITHM/1회차/김유영/20220726/7_나는 요리사다.txt","r")

max = 0
max_i = 0
for i in range(1, 6):
    # 각 숫자 리스트의 합을 구함
    # str형식을 쉽게 특정 형식으로 바꿀 수 있도록 
    score_sum = sum(list(map(int, input().split())))
    if score_sum > max:   # 가장 많은 점수를 얻은 사람
        max = score_sum
        max_i = i

print(max_i, max)