# https://www.acmicpc.net/problem/2941
# 문제2941번.크로아티아 알파벳
# 시간제한:1초, 메모리제한:128MB



# 입력
'''
1. 크로아티아 단어
- 0 < 단어 길이 <= 100
- 알파벳 소문자와 '-', '='으로만 이루어져 있음
'''



# 출력
'''
1. 단어가 몇 개의 크로아티아 알파벳으로 이루어져 있는지 출력
<크리아티아 알파벳>
-두개의 조합으로 된 알파벳: c=, c-, dz=, d-, lj, nj, s=, z=
- 위에 없는 알파벳은 한 글자씩 셈
'''



# 코드 1
import sys

sys.stdin = open('input_text/2941.txt')

word = input()
# 두세글자 크로아티아 알파벳
alphs = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
cnt = 0   # 알파벳 갯수 카운트
idx = 0   # word 슬라이싱의 시작 인덱스
while idx < len(word):
    for alph in alphs:
        # word 슬라이싱이 alphs 내 알파벳(두세글자 알파벳)에 해당하는 경우
        if word[idx: idx + len(alph)] == alph:
            cnt += 1
            idx += len(alph)
            break
    # for문에서 break 없이 빠져나온 경우
    # word 슬라이싱이 한글자 알파벳에 해당하는 경우
    else:
        cnt += 1
        idx += 1
print(cnt)



# 실행결과(메모리:30840KB, 시간:68ms)



# 코드 2
sys.stdin = open('input_text/2941.txt')

word = input()
word_list = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

for i in word_list:
    if i in word:
        word = word.replace(i, '*')

print(len(word))



# 실행결과(메모리:30840KB, 시간:68ms)
