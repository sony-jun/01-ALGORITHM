
# 순회 할 때, 각 인자의 값이 증가해야지 오르막길 즉, 부분 수열이 된다.
# 리스트를 만들어서 인덱스 끝과 처음을 빼볼까 생각했지만 시간 너무 많이 걸림
# 그래서 리스트 안을 순환하면서 그 다음 인덱스와 첫 인덱스의 차를

T = int(input()) # 수열의 크기 즉 수열의 길이 - 입력

arr = list(map(int, input().split())) # 수열 안에 들어가는 Tㄱ

dif = 0 # 차이값
dif_list = []
for i in range(T-1): # out of range 해결
    if arr[i] - arr[i+1] < 0:
        dif += arr[i+1] - arr[i]
        dif_list.append(dif)
    if arr[i] - arr[i+1] >= 0:
        dif = 0


if len(dif_list) == 0:
    result = 0
else:
    result = max(dif_list)

print(result)
        
