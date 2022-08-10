import sys
input = sys.stdin.readline

w = [int(input())for _ in range(10)] # w 대학 점수 리스트
k = [int(input())for _ in range(10)] # k 대학 점수 리스트

w.sort(reverse=True) #내림차순으로 정렬
k.sort(reverse=True)
# print(w)
# print(k)
w_score = w[0] + w[1] + w[2] #가장 큰 세 값만 더하기
k_score = k[0] + k[1] + k[2] 

print(w_score, k_score)