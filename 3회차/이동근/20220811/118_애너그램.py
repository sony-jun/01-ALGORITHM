import sys

input = sys.stdin.readline

T = int(input())

for _ in range(T):
    A, B = input().split()

    result = "anagrams."

    if sorted(A) != sorted(B): 
        result = "NOT " + result

    print(A, '&', B, "are", result)