import sys

input = sys.stdin.readline

for test_case in range(int(input())):
    n, m = map(int, input().rstrip().split())
    answer = 0
    for i in range(n, m + 1):
        answer += str(i).count("0")
    print(answer)