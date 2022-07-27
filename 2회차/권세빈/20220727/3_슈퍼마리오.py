# https://www.acmicpc.net/problem/2851
import sys

sys.stdin = open("3.txt", "r")

sum_ = 0
for i in range(10):     # 10개 버섯들
    n = int(input())    # 점수 입력값 받기
    sum_ += n           # 점수 합치기
    if sum_ >= 100:     # 만약 100보다 같거나 크다면
        if sum_ - 100 > 100 - (sum_ - n):   # 100을 넘겼을 때 값을 더한 값과 값을 더하지 않은 값을 비교
            sum_ -= n                       # 차이가 더 적은 쪽을 출력한다.
        break
print(sum_)             # 100보다 작을 땐 if문 실행 안하고 그냥 바로 print됨   