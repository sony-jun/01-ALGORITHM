# 1157.
"""
"""
import sys
sys.stdin = open("단어공부.txt")

words = input()
# 알파벳 등장횟수를 저장할 딕셔너리
wordict = {}
for char in words:
    if ord(char) > 90:
        char = chr(ord(char) - 32)
    wordict[char] = wordict.get(char, 0) + 1

max_ = max(wordict.values())

# 중복되는 횟수
cnt = 0
max_list = []

for key in wordict:
    if wordict[key] == max_:
        cnt += 1
        max_list.append(key)
    
    if cnt >= 2:
        print("?")
        break
        
else:
    for elem in max_list:
        print(elem, end="")