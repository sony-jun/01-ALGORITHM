# 5800.
""" 
"""
import sys
sys.stdin = open("성적통계.txt")
from collections import deque

T = int(input())
for t in range(1, T+1):
    # 입력받은 내용 분리하기
    list_ = list(map(int, input().split()))
    list_ = deque(list_)
    N = list_.popleft()
    # print(N)
    score = list(list_)
    # print(score)
    max_num = 0
    min_num = 0
    
    for idx in range(len(list))
    
    
    
    
    
    
    
    
    
    
    
    # print(f'"Max {max_num}, Min {min_num}, Largest gap {gap}"')