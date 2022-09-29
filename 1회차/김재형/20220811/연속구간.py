import sys
sys.srdin = open('연속구간_input.txt')

for i in range(3):
    num = input()
    cnt = 1
    count = []
    for n in range(1, len(num)):
        if num[n-1] == num[n]:
            cnt += 1
            count.append(cnt)
        if num[n-1] != num[n]:
            cnt = 1
    if len(count) == 0:
        print(1)
    else:
        print(max(count))