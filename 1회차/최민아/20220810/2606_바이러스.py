import sys
sys.stdin = open("20220810/2606_바이러스.txt")

PC = int(input())                       # 컴퓨터 개수 = 정점
connect = int(input())                  # 서로 연결된 컴퓨터 쌍의 수 = 간선

network = [[] for i in range(PC+1)]     # 네트워크 상태 인접 리스트
for i in range(connect):
    x, y = map(int, input().split())    # 연결된 컴퓨터 두 대 번호
    network[x].append(y)                # 인접 리스트에 추가
    network[y].append(x)                # 인접 리스트에 추가

visited = []                            # 바이러스 감염 컴퓨터
def virus(start):                       # 시작 컴퓨터 번호 받는 함수 virus
    for i in network[start]:            # 해당 컴퓨터 번호와 연결된 컴퓨터
        if i not in visited:            # visited에 번호가 없으면
            visited.append(i)           # 감염 컴퓨터로 번호 추가
            virus(i)                    # 연결된 컴퓨터까지 순회

virus(1)                                # 1번이 웜 바이러스에 걸렸을 때
print(len(visited)-1)                   # 1번을 제외한 감염 컴퓨터 수 출력