# 2511

import sys
sys.stdin = open("카드놀이.txt")

# A리스트, B리스트 받아오기
A_list = list(map(int, input().split()))
B_list = list(map(int, input().split()))

winner = 'D'
A = 0
B = 0
for idx in range(10):
    if A_list[idx] > B_list[idx]:
        A += 3
        winner = 'A'
    
    elif A_list[idx] < B_list[idx]:
        B += 3
        winner = 'B'
        
    else:
        A += 1
        B += 1
        
print(A, B)

if A > B:
    print('A')
elif B > A:
    print('B')
else:
    print(winner)