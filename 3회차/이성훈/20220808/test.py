# https://www.acmicpc.net/problem/1543
import sys

sys.stdin = open("3_문서 검색.txt")

word = input()
search = input()
cnt = 0
print(word.count(search))
