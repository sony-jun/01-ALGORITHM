import sys
sys.stdin = open('11_덩치.txt')

N = int(input())
big = []
for i in range(N):
    big.append(list(map(int, input().split())))

#1등으로 시작해서 자기보다 키, 몸무게 둘 다 큰 사람을 발견할때마다 등수 올리기
for i in big:
    answer = 1
    for k in big:
        if i[0] < k[0] and i[1] < k[1]:
            answer += 1
    print(answer, end=' ')
