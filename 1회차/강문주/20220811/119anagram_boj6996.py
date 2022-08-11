import sys
sys.stdin =open("boj4963.txt")
input = sys.stdin.readline

T = int(input())

for i in range(T):
    a, b = map(str,input().split())
    x = sorted(a)
    y = sorted(b)

    if x == y:
        print(a, "&", b, "are anagrams.")
    else:
        print(a, "&", b, "are NOT anagrams.")