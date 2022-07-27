# https://www.acmicpc.net/problem/2941

import sys
sys.stdin = open("/Users/yuyeong/Desktop/알고리즘/01-ALGORITHM/1회차/김유영/20220727/10_크로아티아 알파벳.txt")

A = ('c=','c-','dz=','d-','lj','nj','s=','z=')
B = input()
for i in A:
    # 문자열에서 값을 찾아준다. 
    B = B.replace(i, 'A')
# 길이를 출력한다.
print(len(B))