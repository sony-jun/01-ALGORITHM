# https://www.acmicpc.net/problem/2577
import sys, collections

sys.stdin = open("0_숫자의개수.txt")

A=int(input())
B=int(input())
C=int(input())

num_list=list(str(A*B*C)) # A,B,C의 곱을 문자열로 변환하여 리스트로 변환한다.
dict_num = collections.Counter(num_list) # Counter 클래스를 사용하여 리스트의 원소 개수를 딕셔너리로 반환

for i in range(10):
    print(dict_num[str(i)]) # 0 ~ 9까지 순회하면서 출력