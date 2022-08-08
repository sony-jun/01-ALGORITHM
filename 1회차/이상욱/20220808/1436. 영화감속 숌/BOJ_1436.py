import sys
sys.stdin = open('1436.txt')
n = int(input())
number = 666
cnt = 0

while True:
    if '666' in str(number): # 숫자에 666이 포함되어 있는 경우
        cnt += 1            # cnt 값에 1 더한다
    if cnt == n:            # cnt 값이 n의 값과 같을 경우 while반복문을 끝낸다
        print(number)
        break
    number += 1 # 반복문이 끝날 때 까지 매번 사이클 마다 1씩 더해준다.

# cnt가 2일 경우
# 처음 if문에서 cnt += 1 >> cnt = 1
# number += 1 >> number = 667
# 반복문을 돌다가 1666에서 cnt가 2가됨
# cnt == n이니까 반복문 종료