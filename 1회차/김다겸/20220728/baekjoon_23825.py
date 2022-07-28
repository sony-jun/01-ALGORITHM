n, m = map(int,input().split())

# s 블록 개수
s = n // 2
# a 블록 개수
a = m // 2

# s와 a 둘다 있어야하므로 s, a의 최소값
print(min(s, a))