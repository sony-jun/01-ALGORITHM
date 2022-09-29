# BOJ - 1003

test = int(input())
for t in range(test):
    zero = [1, 0]
    one = [0, 1]
    n = int(input())
    for i in range(n - 1):
        zero.append(zero[i] + zero[i + 1])
        one.append(one[i] + one[i + 1])

    if n == 0:
        print(1, 0)
    else:    
        print(zero[-1], one[-1])