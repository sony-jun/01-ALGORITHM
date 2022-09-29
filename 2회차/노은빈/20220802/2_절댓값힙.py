import sys
import heapq
input = sys.stdin.readline

n =int(input())  #연산의 개수
heap = []        #heap 생성

for i in range(n):         #n만큼
    numbers = int(input()) #여러줄로 숫자 받기
    if numbers != 0:       #정수가 0이 아니면
        heapq.heappush(heap, (abs(numbers), numbers))  #abs 는 구글링함 -> 튜플로 넣음
    else :
        if heap:   #정수가 0이면 0출력-> 이 부분도 구글링 답이 안 나왔음
            print(heapq.heappop(heap)[1])#heap에 절댓값이 가장 작은 값 출력 후 제거      
        else:
            print(0)    