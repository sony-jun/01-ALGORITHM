import sys
sys.stdin = open('유니크.txt','r')

N = int(input()) #참가자의 수

matrix = [list(map(int,input().split())) for _ in range(N)]

print(matrix)
for n in range(N): #참가자의 수만큼 반복 n: 몇번쨰 사람인가
    sum = 0
    for m in range(3): #3번의 게임을 한다 m: 몇번쨰 경기인가
        cnt = 0
        for n_ in range(N): #비교할 값을 가져와서 반복한다. 반복문에 자신이 포함되므로 cnt는 2로 측정
            if matrix[n][m] == matrix[n_][m]:
                cnt += 1
            if cnt == 2 :
                sum += 0
                break
        else:
            sum += matrix[n][m]
    print(sum)