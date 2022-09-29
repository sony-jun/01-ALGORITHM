import sys

sys.stdin = open('boj2851.txt')

result = int(input())

for i in range(0,9):
    n = int(input())
    if abs(result - 100) >= abs(result + n - 100):
        result += n
    else:
        print(result)
        break
else:
    print(result)

