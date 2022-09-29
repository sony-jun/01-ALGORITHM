# 백준 9012
import sys

# input = sys.stdin.readline
sys.stdin = open('괄호.txt', 'r')


t = int(input())

for _ in range(t):
    check = input()
    ls = list(check)
    sum = 0

    for i in ls:
        if i == '(':
            sum += 1
        elif i == ')':
            sum -= 1
        if sum < 0:
            print('NO')
            break

    if sum > 0:
        print('NO')
    elif sum == 0:
        print('YES')

# ( 가 나올 때는 1을 더하고 ) 가 나올 때는 1을 빼서
# 최종 sum이 0이 되면 끝

# t 변수로 테스트 케이스의 수를 입력 받고
# for 문을 통해 테스트 케이스 수만큼 반복하면서
# 그 안에서 check할 문자열을 입력 받음

# check 변수로 받은 문자열은 ls 변수로 list로 입력 받고
# 1을 더하고 빼주는 것을 기록할 sum 변수를 만들어 0으로 초기화

# for 문 안에 sum이 0보다 작아질 때
# 즉 ) 가 나와서 sum에 -1이 축적되어 조건을 만족하지 못할 때
# no 를 출력하고 break

# 나머지는 sum이 0보다 크다면 문자열에 ( 가 하나 더 있는거니
# 조건에 만족하지 못하여 no 출력
# 마지막으로 else가 아니라 elif를 써서
# 또 하나의 조건문으로 sum이 0일 때만
# 즉, 딱 ( 와 ) 가 만나서 0이 될 때만 yes를 출력