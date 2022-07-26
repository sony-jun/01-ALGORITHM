# https://www.acmicpc.net/problem/2231
# 문제2231번.분해합
# 시간제한:2초, 메모리제한:192MB



# 입력
'''
1. 자연수 N
- 1 <= N <= 1,000,000
'''



# 출력
'''
1. 자연수 N의 가장 작은 생성자를 출력
- N(245)의 분해합 = N(245) + N을 이루는 각 자리수(2 + 4 + 5) = M(256)
- N은 M의 생성자(245는 256의 생성자)
- 245 --분해합--> 256
- 245 <--생성자-- 256
- 생성자가 없는 자연수가 있을 수 있음
- 생성자가 여러 개인 자연수가 있을 수 있음
- 생성자가 없는 경우에는 0을 출력
'''



# 코드 1
import sys

sys.stdin = open('input_text/2231.txt')

num = int(input())
rst = 0

# num의 생성자 == 분해합했을 때 num이 되는 수
# 1부터 num까지 분해합했을 때 num이 나오는지 확인
for n in range(1, num):
    now_n = n   # 아래에서 n값을 변형시킬 것이므로, 미리 다른 변수에 값 복제
    # 분해합 구하기
    decom_sum = n
    while n:
        decom_sum += n % 10
        n //= 10
    # 분해합한 값이 num이면, n은 num의 생성자
    if decom_sum == num:
        rst = now_n
        break

# num의 생성자 출력
print(rst)
    


# 실행결과(메모리:30840KB, 시간:1220ms)



# 코드 2
sys.stdin = open('input_text/2231.txt')

N = int(input())
# 반복 시작값 구하기
start = N - len(str(N)) * 9 if (N - len(str(N)) * 9) > 0 else 1

# start부터 num까지 분해합했을 때 num이 나오는지 확인
rst = 0
for n in range(start, N):
    now_n = n   # 아래에서 n값을 변형시킬 것이므로, 미리 다른 변수에 값 복제
    # 분해합 구하기
    decom_sum = n
    while n:
        decom_sum += n % 10
        n //= 10
    # 분해합한 값이 N이면, n은 N의 생성자
    if decom_sum == N:
        rst = now_n
        break
print(rst)



# 실행결과(메모리:30840KB, 시간:68ms)