# https://www.acmicpc.net/problem/2577
import sys

sys.stdin = open("0_숫자의개수.txt")

# 입력값 한줄씩 나오게 하기
a = int(input())
b = int(input())
c = int(input())

ans = list(str(a * b *c)) #곱한 값을 문자열로 변환하여 list로 반환

for i in range(10): # i = 0~9
    print(ans.count(str(i))) # list요소가 몇개인지 세기
# 3
# 1
# 0
# 2
# 0
# 0
# 0
# 2
# 0
# 0