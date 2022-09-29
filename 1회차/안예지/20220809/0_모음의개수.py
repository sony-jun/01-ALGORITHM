# 1264.
"""
접근방법
1. 개행을 기준으로 문장을 입력받는다.
"""
import sys
sys.stdin = open("모음개수.txt")
from collections import deque

words = ['0'] # 인덱스 오류를 방지하기 위해 임의의 요소
while words[-1] != '#':
    words.append(input())

for i in words:
    aeiou = 0
    if i != '0' and i != '#':
        for chr in i:
            if chr in 'aAeEiIoOuU':
                aeiou += 1
        print(aeiou)