import sys
sys.stdin = open("104_바이러스_2606.txt", "r")

# 인접 리스트 생성 후 재귀?
# adj: 인접 리스트
# result: 감염 여부 리스트 <- 구글링
# 인접 리스트adj를 순회하며, 자식 리스트의 요소를 => 감염 여부 리스트result에 표시

N = int(input()) # 노드
M = int(input()) # 엣지

# 인접 리스트 생성
adj = [[] for _ in range(N+1)]

for i in range(M):
    u, v = map(int, input().split())
    adj[u].append(v)
    adj[v].append(u)

# 감염시키면 1, 아니면 0
result = [0 for _ in range(N+1)] # [1, 0, 0, 1, 0...]

# 감염 대수, 재귀를 위해 함수 바깥에
cnt = 0

def virus(index):
    # 글로벌 변수 가져옴
    global cnt                      # 없으면: UnboundLocalError: local variable 'cnt' referenced before assignment
    
    # 감염된 컴퓨터 위치를, result에 표시
    result[index] = 1               # +=1이 아닌 이유: True(1) / False(0)를 따지는 것이기 때문에

    
    for i in adj[index]:            # 자식 리스트 순회하며
        if result[i] == 0:          # 감염 여부 리스트에 표시된 적 없으면
            virus(i)                # 함수 재귀 후
            cnt += 1                # cnt 세어줌
    
    return True

virus(1)                            # 문제 조건

print(cnt)
