import sys
sys.stdin = open("20220808/1436_영화감독숌.txt")

N = int(input())            # 구해야 하는 종말의 숫자

num = 666                   # 숫자 num, 666으로 시작
cnt = 0                     # 몇 번째 종말의 숫자인가
while(True):
    if '666' in str(num):   # num에 666이 들어가면
        cnt += 1            # cnt번째 종말의 숫자
        if cnt == N:        # 현재 cnt와 구해야하는 N번이 같으면
            print(num)      # 현재 num 출력
            break           # 반복문 탈출
    num += 1                # num을 1씩 증가시키면서 반복문 진행

    # 666 1666 2666 3666 4666 5666 6660 6661 6662 ... 6669 7666 ...