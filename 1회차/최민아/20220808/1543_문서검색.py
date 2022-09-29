import sys
sys.stdin = open("20220808/문서검색.txt")

word = input()
find = input()

word = word.replace(find, '*')
cnt = word.count('*')

print(cnt)