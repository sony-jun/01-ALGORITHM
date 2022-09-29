# https://www.acmicpc.net/problem/2857
import sys
sys.stdin = open('B2857.txt')

FBI = []
for i in range(1, 6):
    code_name = input()
    if 'FBI' in code_name:
        FBI.append(i)

if len(FBI) > 0:
    print(*FBI)
else:
    print('HE GOT AWAY!')   
