import sys

sys.stdin = open("3_영화감독 숌.txt")

n = int(input())
movie = 666

while n:
    if "666" in str(movie):
        n -= 1
    movie += 1

print(movie - 1)