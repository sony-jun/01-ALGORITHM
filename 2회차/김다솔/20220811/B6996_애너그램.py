# https://www.acmicpc.net/problem/6996
import sys
sys.stdin = open('B6996.txt')

T = int(input())
for tc in range(T):
    A, B = input().split()
    # print(sorted(list(A)), sorted(list(B)))    
    if sorted(list(A)) == sorted(list(B)):
        print(f'{A} & {B} are anagrams.')
    else:
        print(f'{A} & {B} are NOT anagrams.')