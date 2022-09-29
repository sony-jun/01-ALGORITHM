# BOJ - 2747

fibo = [0, 1]
n = int(input())
for i in range(n - 1):
    fibo.append(fibo[i] + fibo[i + 1])
print(fibo[n])