N,M = map(int,input().split())
lit = list(map(int,input().split()))
result = []
for i in range(N):
    for j in range(i+1,N): # 각 1씩더해준 이유는 i부터 시작하면 인덱스가 겹쳐버리기 때문.
        for k in range(j+1,N):# 마찬가지.
            x = lit[i] + lit[j] + lit[k]
            if x > M:
                continue
            else:
                result.append(x)
print(max(result))

# for 문을 삼중으로 받아야 하는데 이때 인덱스가 겹치지 않게 하기 위해 각 값에 1을 더해주었습니다.
# x 라는 lit 내의 값을 더한 변수를 선언 한 후
# x 를 기준으로 M 보다 클경우엔 넘어가고 작거나 같을시엔 result라고 선언해둔 리스트에 append 하여 
# 그 값중 가장 큰 값을 출력하게 구성하였습니다.