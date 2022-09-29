import heapq

n = int(input())
heap = []

# input받은 값을 heap 리스트에 추가하기
for i in range(n):
    heap.append(int(input()))

# heap 리스트 순회
for i in range(len(heap)):
    # heap 리스트를 heapq 형태로 정렬
    heapq.heapify(heap)
    # heap의 맨 처음 값(가장 작은 값) 출력
    print(heapq.heappop(heap))