import sys
sys.stdin = open("가장큰금민수.txt")

N = int(input()) #N문자버저


for number in range(N,3,-1):
    number_str = str(number)
    cnt = 0
    for s in number_str:
        if s == '4' or s == '7':
            cnt += 1

    if cnt == len(number_str):
        print(number)
        break
    cnt = 0