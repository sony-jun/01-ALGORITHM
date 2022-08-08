# https://www.acmicpc.net/problem/1543
# 문제1543번.문서 검색
# 시간제한:2초, 메모리제한:128MB



# 입력
'''
1. 문서
- 0 < 문서의 길이 <= 2,500
2. 검색하고 싶은 단어
- 0 < 단어 길이 <= 50
'''



# 출력
'''
1. 중복되지 않게 최대 몇 번 등장하는지 출력
'''



# 코드 1
import sys

sys.stdin = open('input_text/1543.txt')

s = input()
word = input()

start = 0   # 슬라이싱 시작 인덱스
cnt = 0   # 문서s 내 단어 word의 갯수
while start + len(word) <= len(s):
    if s[start:start + len(word)] == word:
        cnt += 1
        start += len(word)
    else:
        start += 1

print(cnt)



# 실행결과(메모리:30840KB, 시간:72ms)



# 코드 2
import sys

sys.stdin = open('input_text/1543.txt')

s = input()
word = input()

print(s.replace(word, '*').count('*'))



# 실행결과(메모리:30840KB, 시간:84ms)



# 코드 3
import sys

sys.stdin = open('input_text/1543.txt')

s = input()
word = input()

print(s.count(word))



# 실행결과(메모리:30840KB, 시간:68ms)