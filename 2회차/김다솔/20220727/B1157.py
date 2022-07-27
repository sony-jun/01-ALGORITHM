# https://www.acmicpc.net/problem/1157
# 대소문자 구분 없이 가장 많이 쓰인 알파벳 찾기 
# 다 대문자나 소문자로 바꿔놓고 중복 없이 리스트에 모아서 카운트 
# if max 값 두개 이상이면 ? 출력 

import sys
sys.stdin = open('B1157.txt')

word = input().upper() # 입력받으면서 바로 다 대문자로 바꾸는 함수 적용
alph = list(set(word)) # 알파벳 중복없이 걸러서 리스트로 만들기
# print(alph) ['M', 'P', 'S', 'I']
cnt = [] # 알파벳 당 빈도 카운트해서 담을 빈 리스트

for i in alph: # 중복없이 쓰인 알파벳 하나씩 반복할 동안
    # count_ = word.count(i) 원래 단어에서 지금 순서 알파벳 몇 번 썼는지 카운트
    # print(count) 1 4 4 1
    cnt.append(word.count(i)) # 카운트 값을 미리 만들어놓은 빈 리스트에 넣기
    # print(cnt)
    
if cnt.count(max(cnt)) < 2: # 젤 큰 수가 중복이 아니면 
    print(alph[(cnt.index(max(cnt)))]) # 중복 없는 리스트랑 카운트한 리스트랑 인덱스 위치 알파벳 같으니까 
    # [b, a] [1, 3]
else:
    print('?')
    