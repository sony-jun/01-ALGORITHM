# https://www.acmicpc.net/problem/1157
import sys
sys.stdin = open("1157.txt")
word = input().upper()
set_ = list(set(word))

cnt = [word.count(i) for i in set_]

if cnt.count(max(cnt)) > 1:
  print("?")

else:
  print(set_[(cnt.index(max(cnt)))])