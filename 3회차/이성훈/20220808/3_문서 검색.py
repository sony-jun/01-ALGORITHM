# https://www.acmicpc.net/problem/1543
import sys

sys.stdin = open("3_문서 검색.txt")

T = input()                             # 전체단어
word_ = input()                         # 찾는 단어
n = 0
cnt = 0

while n <= len(T) - len(word_):         # 돌아야 할 숫자  9 - 3
    if T[n:n + len(word_)] == word_:    # 전체 문자에서 단어만큼 길이 슬라이싱이 단어와 같은지 비교
        cnt += 1                        # 맞으면 1증가
        n += len(word_)                 # 맞으면 단어 길이만큼 n 증가
    else:                               
        n += 1                          # 틀리면 1만큼 증가

print(cnt)

