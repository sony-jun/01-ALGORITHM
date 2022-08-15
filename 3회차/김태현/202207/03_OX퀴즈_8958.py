import sys
sys.stdin = open("03_OX퀴즈_8958.txt", "r")

T = int(input())

for i in range(1, T+1):
    ox = input()
    score = 0
    seq = 0

    for j in range(len(ox)):
        if ox[j] == "O":
            seq += 1
            score += seq
        else:
            seq = 0
    print(score)
