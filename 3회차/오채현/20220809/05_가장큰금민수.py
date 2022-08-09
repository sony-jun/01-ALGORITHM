n = int(input())

# n = 100

while True:
    N = str(n)
    a = len(N)
    if a == N.count('4') + N.count('7'):
        print(n)
        break
    n -= 1
