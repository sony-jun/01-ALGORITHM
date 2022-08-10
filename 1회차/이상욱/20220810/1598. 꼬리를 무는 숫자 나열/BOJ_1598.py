import sys
sys.stdin = open('1598.txt')

A, B = map(int, input().split())

A_r = ((A-1)//4)
B_r = ((B-1)//4)

A_c = ((A-1)%4)
B_c = ((B-1)%4)

print(abs(A_r - B_r) + abs(A_c - B_c))