# https://www.acmicpc.net/problem/1357

import sys
sys.stdin = open("/Users/yuyeong/Desktop/알고리즘/01-ALGORITHM/1회차/김유영/20220728/17_뒤집힌 덧셈.txt")


X, Y = map(str, input().split())
# 문자열로 입력 받아 뒤집어준다.
S = str(int(X[::-1])+ int(Y[::-1]))
# 다시 정수형으로 바꾼다.
print(int(S[::-1]))