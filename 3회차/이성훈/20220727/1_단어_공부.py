# https://www.acmicpc.net/problem/1157
import sys

sys.stdin = open("1_단어_공부.txt")

T_list = []
T = input().lower()
set_T = list(set(T))                                    # set이면 인덱싱 못해서 list 시켜야함

for i in set_T:
    num = T.count(i)
    T_list.append(num)

if T_list.count(max(T_list)) >= 2 :
    print('?')
else:
    print(set_T[T_list.index(max(T_list))].upper())     #


    
    
