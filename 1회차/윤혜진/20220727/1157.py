# https://www.acmicpc.net/problem/1157
# 문제1157번.단어공부
# 시간제한:2초, 메모리제한:128MB



# 입력
'''
1. 알파벳 대소문자
- 0 < 단어의 길이 <= 1,000,000
'''



# 출력
'''
1. 단어에서 가장 많이 사용된 알파벳을 대문자로 출력
- 단, 가장 많이 사용된 알파벳이 여러 개 존재하는 경우에는 '?'을 출력
- 대문자와 소문자는 구분하지 않음
'''



# 코드 1
import sys

sys.stdin = open('input_text/1157.txt')

word = input()

# 알파벳 a ~ z --ord()--> 97 ~ 122
# 알파벳 A ~ Z --ord()--> 65 ~ 90
# 알파벳 A ~ Z => 리스트의 인덱스 0 ~ 25
cnt = [0] * 26   # 인덱스: A ~ Z, 값: 각 알파벳 등장 횟수

for char in word:
    # 소문자인 경우, 소문자 -> 대문자 바꾼 후 카운트 세기
    if 97 <= ord(char) <= 122:
        idx = (ord(char) - 32) - 65
        cnt[idx] += 1
    # 대문자인 경우, 바로 카운트 세기
    elif 65 <= ord(char) <= 90:
        idx = ord(char) - 65
        cnt[idx] += 1

# cnt 리스트를 돌면서 가장 많이 등장한 알파벳 출력
max_alph = ''
max_cnt = 0
for i in range(0, len(cnt)):
    if max_cnt < cnt[i]:
        max_cnt = cnt[i]
        max_alph = chr(i + 65)
    elif max_cnt == cnt[i]:
        max_alph += chr(i + 65)

print('?' if len(max_alph) > 1 else max_alph)



# 실행결과(메모리:32796KB, 시간:468ms)



# 코드 2
sys.stdin = open('input_text/1157.txt')

word = input().upper()
cnt = [0] * 26   # 인덱스: A ~ Z, 값: 각 알파벳 등장 횟수
for char in word:
        idx = ord(char) - 65
        cnt[idx] += 1

# cnt 리스트를 돌면서 가장 많이 등장한 알파벳 출력
max_alph = ''
max_cnt = 0
for i in range(0, len(cnt)):
    if max_cnt < cnt[i]:
        max_cnt = cnt[i]
        max_alph = chr(i + 65)
    elif max_cnt == cnt[i]:
        max_alph += chr(i + 65)

print('?' if len(max_alph) > 1 else max_alph)



# 실행결과(메모리:32796KB, 시간:288ms)



# 코드 3
import collections

sys.stdin = open('input_text/1157.txt')

word = input().upper()
cnt = collections.Counter(word)
max_2 = cnt.most_common(n=2)

if len(max_2) == 1:
    print(max_2[0][0])
else:
    if max_2[0][1] == max_2[1][1]:
        print('?')
    else:
        print(max(max_2, key=lambda x: x[1])[0])



# 실행결과(메모리:33888KB, 시간:148ms)