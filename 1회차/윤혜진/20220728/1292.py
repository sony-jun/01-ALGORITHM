# https://www.acmicpc.net/problem/1292
# 문제1292번.쉽게 푸는 문제
# 시간제한:2초, 메모리제한:128MB



# 입력
'''
1. 구간의 시작, 끝을 나타내는 정수 A, B
- 1 <= A, B <= 1,000
'''



# 출력
'''
1. 구간에 속하는 숫자의 합을 출력
- 수열: 1 2 2 3 3 3 4 4 4 4 5 5 5 5 5...
- 위 수열에서 A번째 숫자부터 B번째 숫자까지의 합을 출력
'''



# 코드 1
import sys

sys.stdin = open('input_text/1292.txt')

# 수열 생성
seq = [0]
num = 1
while len(seq) <= 1000:
    seq += [num] * num
    num += 1

# 구간합 구하기
A, B = map(int, input().split())
sub_sum = 0
for idx in range(A, B + 1):
    sub_sum += seq[idx]

print(sub_sum)



# 실행결과(메모리:30840KB, 시간:72ms)



# 코드 2
sys.stdin = open('input_text/1292.txt')

# 인덱스 0부터 1000까지 누적합을 구해 리스트에 담기
acc = [0]   
num = 1   # 더해야하는 숫자
cnt = num   # 해당 숫자를 더한 횟수 카운트
idx = 0   # acc의 인덱스
while idx <= 1000:
    # 특정 숫자를 해당 숫자만큼 모두 더했으면, 다음 숫자로 넘어가기
    if cnt == 0:
        num += 1
        cnt = num
        continue
    # 특정 숫자를 해당 숫자만큼 누적해서 더하기
    acc.append(acc[idx] + num)
    cnt -= 1
    idx += 1

# 구간합 구하기
A, B = map(int, input().split())
print(acc[B] - acc[A - 1])



# 실행결과(메모리:30840KB, 시간:72ms)



# 코드 3
sys.stdin = open('input_text/1292.txt')

A, B = map(int, input().split())

seq = []
for b in range(1, B + 1):
    seq += [b] * b

print(sum(seq[A-1:B]))



# 실행결과(메모리:35176KB, 시간:76ms)
