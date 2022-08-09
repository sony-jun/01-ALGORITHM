import sys
sys.stdin = open("20220809/2606_바이러스.txt")

PC = int(input())                       # 컴퓨터 개수 = 정점
connect = int(input())                  # 서로 연결된 컴퓨터 쌍의 수 = 간선

network = [[] for i in range(PC+1)]     # 네트워크 상태 인접 리스트
for i in range(connect):
    x, y = map(int, input().split())    # 연결된 컴퓨터 두 대 번호
    network[x].append(y)                # 인접 리스트에 추가
    network[y].append(x)                # 인접 리스트에 추가

result = [0 for i in range(PC+1)]       # 감염 여부
cnt = 0                                 # 바이러스에 감염된 컴퓨터 수

def virus(index):
    global cnt

    result[index] = 1                   # 해당 컴퓨터는 감염으로 표시

    for i in network[index]:            # 감염 컴퓨터의 인접 컴퓨터 확인
        if result[i] == 0:              # 인접 컴퓨터가 감염 표시가 0이면
            virus(i)                    # 재귀 함수 수행
            cnt += 1                    # 감염된 컴퓨터 수 +1
    
    return True

virus(1)                                # 문제에서 주어진 감염 컴퓨터 번호

print(cnt)                              # 최종 감염 수 출력