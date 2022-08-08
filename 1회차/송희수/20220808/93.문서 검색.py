import sys

sys.stdin = open("93.문서 검색.txt")

word = input()
find = input()

# 단어 등장 개수
cnt = 0

while find in word:
    for i in range(len(word)):
        if word[i : i + len(find)] == find:
            word = word[i + len(find):]
            break
    cnt += 1

print(cnt)


