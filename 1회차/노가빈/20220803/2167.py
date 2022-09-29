
n, m = map(int,input().split(' '))

list2d = [] #2차원 배열을 선언

for i in range(n):
    list2d.append(input().split(' ')) # 2차원 배열 넣기
# print(list2d) 출력: [['1', '2', '4'], ['8', '16', '32']]

t = int(input())
for i in range(t):
    i,j,x,y = map(int, input().split(' '))
    score = 0
    
    if i==x and j == y: # 열과 행이 같으면
        score += int(list2d[i-1][j-1]) # 그대로 더함
        print(score)
    else:
        for k in range(i,x):
            for z in range(j,y):
                score += int(list2d[i-1][j-1])
                print(list2d[i-1][j-1])
        print(score)