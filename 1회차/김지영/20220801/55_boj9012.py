import sys
sys.stdin = open("input.txt")
T = int(input())
for test_case in range(1,T+1):
    br = input()
    c = 0
    while True:
        c += 1
        br = br.replace('()','')

        if '()' not in br:
            break
    # result = br
    if len(br) != 0:
        result = 'NO'
    else : result = 'YES'
    print(f'#{test_case} ',result)
