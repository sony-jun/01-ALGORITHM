import sys

sys.stdin = open("_6996.txt", "r")

for _ in range(int(input())):
    A, B = input().split()

    if sorted(list(A)) == sorted(list(B)):
        print(f"{A} & {B} are anagrams.")
    else:
        print(f"{A} & {B} are NOT anagrams.")