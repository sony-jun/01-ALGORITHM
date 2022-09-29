# https://www.acmicpc.net/problem/2908
import sys

sys.stdin = open("1_상수.txt")

n,m = map(int,input().split())

new_n = str(n)[::-1] # 숫자를 문자열로 치환하여 뒤집는다.
new_m = str(m)[::-1]

print(max(new_n,new_m)) # 더 큰 값을 출력한다.