N, M = map(int, input().split())
park = [input() for _ in range(N)]

dx = [0,1,1]
dy = [1,0,1]
total_list = [[],[],[],[],[]]
for n in range(N-1):
    for m in range(M-1):
        cnt = 0
        for a in range(3):
            if park[n][m] == '.':
                if park[n+dx[a]][m+dy[a]] == '.':
                    cnt += 1
                if park[n+dx[a]][m+dy[a]] == '#':
                    break
            if park[n][m] == 'X':
                if park[n+dx[a]][m+dy[a]] == '.':
                    cnt += 1
                if park[n+dx[a]][m+dy[a]] == '#':
                    break
        
        if cnt == 3:
            total_list[3-cnt].append(1)
        if cnt == 2:
            total_list[3-cnt].append(1)
        if cnt == 1:
            total_list[3-cnt].append(1)
        if cnt == 0:
            total_list[3-cnt].append(1)

for a in total_list:
    print(len(a))