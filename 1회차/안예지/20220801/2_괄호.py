# 9012.
"""

접근 방법 
1. 열린 괄호'('가 나올 때마다 open리스트에 추가한다.
2. 닫힌 괄호가 ')'가 나올때마다 open리스트에서 꺼내서 괄호를 완성한 후 괄호완성 리스트에 저장한다.
3. 괄호 완성 수를 카운트해서 처음 주어진 괄호문의 길이와 나누었을 때 0이 아니면 No,
4. 맞으면 yes를 출력한다.

한계) 열린괄호 없이 닫힌 괄호만 나올 경우?
"""
import sys
sys.stdin = open("괄호.txt")
from collections import deque

T = int(input())

for _ in range(T):
    word = list(input())
    # 괄호가 완성될때마다 추가할 괄호 완성 수
    v_cnt = 0
    # 닫힌 괄호를 저장할 리스트
    open_ = []
    # 괄호가 완성되면 저장할 리스트
    vps_ = []
    for char in word:
        if word[0] != '(':
            break
        if char == '(':
            open_.append(char)
        if len(open_) > 0 and char == ')':
            vps_.append(open_.pop() + char)
            v_cnt += 1
    if v_cnt > 0:
        if word.count('(') == v_cnt:
            print("YES")
        else:
            print("NO")
    else:
        print("NO")