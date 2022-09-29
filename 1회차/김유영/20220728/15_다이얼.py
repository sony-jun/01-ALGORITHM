# https://www.acmicpc.net/problem/5622

import sys
sys.stdin = open("/Users/yuyeong/Desktop/알고리즘/01-ALGORITHM/1회차/김유영/20220728/15_다이얼.txt")

arr = {
    1:' ',
    2:'ABC',
    3:'DEF',
    4:'GHI',
    5:'JKL',
    6:'MNO',
    7:'PQRS',
    8:'TUV',
    9:'WXYZ',
    0:' '
}
n = input()
ans = 0
for num in n:
    for i in range(0, 10):
        if num in arr[i]:
            # 하나 올라갈때가마 1초씩 증가한다. 
            ans += i + 1
            break
print(ans)