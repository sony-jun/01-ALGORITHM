# https://www.acmicpc.net/problem/1598
import sys 
sys.stdin = open('B1598.txt')

n1, n2 = map(int, input().split())
# ran_n1 = n1 - (4 - (n1 % 4))
# ran_n2 = n2 + (4 - (n2 % 4))
# list = [] 굳이 리스트로 안 만들어도 되는 문제,,, 

# 인덱스 개념으로 생각하면 1234 -> 0123 so
n1 -= 1
n2 -= 1
ew = abs(n1//4 - n2//4)
sn = abs(n1%4 - n2%4)
print(ew + sn)
#절대값 함수 안쓰면 음수 나올 수 있음 

