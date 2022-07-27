# https://www.acmicpc.net/problem/2941
import sys

sys.stdin = open("2_크로아티아_알파벳.txt")

str_ = ['c=' , 'c-', 'dz=' , 'd-', 'lj', 'nj', 's=', 'z=']          # 크로아티아 알파벳 리스트 만들기

T = input()                         # 문자열 입력
for i in str_:                      # str_리스트 하나씩 꺼냄
    T = T.replace(i,'1')            # 입력한 문자열에서 크로아티아 알파벳이 있으면 1로 바꿈
print(len(T))                       # 글자수 체크하면 끝
    
