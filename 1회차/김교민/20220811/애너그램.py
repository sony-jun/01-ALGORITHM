import sys
sys.stdin = open('애너그램.txt')
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    a, b = map(str, input().split())
    
    x = sorted(list(a))
    y = sorted(list(b))
    
    if x == y:
        print(a, '&' ,b, 'are anagrams.')
    else:
        print(a, '&' ,b, 'are NOT anagrams.')