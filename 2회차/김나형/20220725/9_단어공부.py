# 알파벳 대소문자로 된 단어가 주어지면, 이 단어에서 가장 많이 사용된 알파벳이 무엇인지 알아내는 프로그램을 작성하시오. 단, 대문자와 소문자를 구분하지 않는다.

from distutils import text_file
import sys

sys.stdin = open("9_단어공부.txt")

text = list(input().upper())
set_text = set(text) # 중복값 제거로 text에서 세어줄(count) 문자만 추출 {'I', 'S', 'M', 'P'}
cnt = []

for i in set_text:
    score = text.count(i)
    cnt.append(score)
if cnt.count(max(cnt))>= 2:
    print('?')
else:
    print(list(set_text)[cnt.index(max(cnt))]) # set 리스트에서 index로 자리 찾기 불가 일대일 대칭 구조인 cnt에서 자리를 찾아넣어줌.




    
    
