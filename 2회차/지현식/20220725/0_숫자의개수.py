import sys

sys.stdin = open("0_숫자의개수.txt")
input = sys.stdin.readline

mul = 1
answer = [0] * 10

for _ in range(3):
    num = int(input())
    mul *= num

for i in str(mul):
    answer[int(i)] += 1

for i in answer:
    print(i)