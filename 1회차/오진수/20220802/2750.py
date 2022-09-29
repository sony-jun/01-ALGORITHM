N=int(input())
a=[]
for k in range(1,N+1):
    a.append(int(input()))#입력  a리스트추가
    a=sorted(a) #a리스트정렬 a할당
for i in range(len(a)):
    print(a[i])#요소출력


==============================================
숫자를 입력받아서 리스트에 넣고 heappop을 해서 최솟값 출력을 반복한다.

import heapq
# 해당 정수까지 오름차순으로 정렬할 정수 입력받기
N = int(input())
numbers = []
for _ in range(N):
    n = int(input())
    numbers.append(n)
    
heapq.heapify(numbers)

for i in range(len(numbers)):
    print(heapq.heappop(numbers))