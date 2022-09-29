N = int(input()) # 수열의 길이
route = list(map(int, input().split())) # 높이의 수열

start = route[0] # 시작점
end = route[1] # 끝점
result = 0 # 높이 = 끝점 - 시작점 

for i in range(1, N):
    if end >= route[i]: # 오르막
        start = route[i]
    else:
        end = route[i] # 내리막
    result = max(result, end-start)
print(result)
