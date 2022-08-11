import sys

sys.stdin = open("_17388.txt", "r")


S, K, H = map(int, input().split())
ap = min(list([S,K,H]))


if S+K+H >= 100:
    print("OK")
else:
    if ap == S:
        print("Soongsil")
    elif ap == K:
        print("Korea")
    else:
        print("Hanyang")