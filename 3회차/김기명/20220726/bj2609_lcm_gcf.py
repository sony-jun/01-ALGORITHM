A, B  = map(int,input().split())

def lcm(A, B) :
    lcmList = []
    
    for i in range(1, A + B):  # A+B를 설정한건 대충 큰수를 집어넣은것.. 에러가 안날수준으로. (A+B는 무조건 A혹은 B보다 크니까)
        for j in range(1, A + B):
            if A * i == B * j and i != j:           #어떠한 자연수 i, j에 대해서, i와 j가 같지 않을 때, A*i와 B*j의 값이 같다면. A * i와 B * j는 A,B의 공배수이게 됨.
                lcmList.append(A * i)               # 일단 집어넣음
    return lcmList[0]                       # 제일 먼저 들어간 수가 낮은 수니까, 0번째 인덱스를 반환.

def gcf(A, B):
    gcfList = []

    for i in range(1, A + 1):                       # 둘중 하나의 수인 A이하인 자연수를 모두 돌면서
        for j in range(1, B + 1):                       # B이하 자연수를 순회
            for k in range(1, B + 1):                   # 동일.
                if i * j == A and i * k == B:               #A이하의 자연수인 i값에 대해서, i * j == A, i * k == B라면 i는 A와 B의 공약수이게 됨.
                    gcfList.append(i)                   # 일단 리스트에 집어넣음
    return gcfList[-1]                                  # 리스트중 마지막 요소가 제일 큰 약수 => 최대공약수. 리턴값으로 반환

print(gcf(A, B))
print(lcm(A, B))            #시간초과임. 한참!! 초과임.