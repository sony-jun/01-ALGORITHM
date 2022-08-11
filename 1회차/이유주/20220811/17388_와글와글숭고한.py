#숭실,고려,한양의 참여도를 수치화.

import sys
sys.stdin = open("input.txt")

university = list(map(int, input().split()))
name = ["Soongsil", "Korea", "Hanyang"]
if sum(university) >= 100:
    print("OK")
elif sum (university) < 100:
    for i in range(3):
        if min(university) == university[i]:
            print(name[i])