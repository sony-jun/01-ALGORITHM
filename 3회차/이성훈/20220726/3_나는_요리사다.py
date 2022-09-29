# https://www.acmicpc.net/problem/2953
import sys

sys.stdin = open("3_나는_요리사다.txt")

N_sum = []

for i in range (5):                             # 5명 참가(5번 반복)
    N = map(int, input().split())               # 평가 결과값 입력
    N_sum.append(sum(N))                        # N_sum값을 리스트 형식으로 저장

print(1+N_sum.index(max(N_sum)), max(N_sum))    # max를 사용하여 최대 값을 찾은 후 index를 사용하여 
                                                # 몇번째 index인지 파악 한 후 +1을 더하여 몇번째인지 나타냄

