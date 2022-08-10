import sys
sys. stdin = open("37_문서검색.txt")


S = input().strip()
word = input().strip()

print(S.count(word))