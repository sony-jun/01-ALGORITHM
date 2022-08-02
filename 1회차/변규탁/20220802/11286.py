from sys import stdin

T = int(stdin.readline())

lst = [] # 100,000
heap_abs = abs(lst) 
A = min(heap_abs)
for _ in range(T):
    number = int(stdin.readline())
    if number != 0:
        lst.append(number)
    else:
        if lst:
            if min(lst) < A:
                print(-A)
                while -A in lst:
                    lst.remove(-A)  
            else:
                print(A)
                while A in lst:
                    lst.remove(A)
        else:
            print(0) 
## 시간초과




# '''
# <문제분석>
# 1. 배열에 정수를 넣는다. (input()) 
#     1) 0이 아니면 배열에 추가 (heappush)
#     2) 0이면 2번을 실행

# 2. 절댓값(abs)이 가장 작은 것 출력하고 / 그 값을 제거(heappop)
#     - 단, 가장 작은 값이 여러개일 때는 가장 작은 수(abs하기전의 값)을 배열에서 제거
#     - 1, -1 ==> -1 

# <세부내용>

# '''
# # <구조>
# import heapq

# 음수힙 = [] 
# 양수힙 = [] 

# # 1. 배열이 비어있는 경우 --> 0을 출력해라 (OK)
# # 2. 배열이 한쪽만 있는 경우 --> 한쪽만 pop 해서 출력해라

# 반복할횟수 = int(input())

# for _ in range(반복할횟수):
#     숫자 = int(input())
    
#     if 숫자 > 0:
#         heapq.heappush(양수힙, 숫자)
#     elif 숫자 < 0:
#         heapq.heappush(음수힙, 숫자)
    
#     else:
#         if 음수힙 == []: 
#             if 양수힙 == []:
#                 print(0)
#             else :
#                 print(heapq.heappop(양수힙))
                
#         else:
#             print(heapq.heappop(음수힙))

        


# import heapq

# n = int(input())
# 음수힙 = [] # 음수를 넣을 큐
# 양수힙 = [] # 양수를 넣을 큐

# for i in range(n):
#     a = int(input())
#     if a < 0:
#         heapq.heappush(음수힙, -a) # 절대값이 작은게 앞에 와야 하므로
#     elif a > 0:
#         heapq.heappush(양수힙, a) # 양수이므로 그대로 최소힙으로 구현
#     ####################################################################
#     else: # a==0:
#         if not 음수힙:
#             if not 양수힙:
#                 print(0)
#     ####################################################################            
#             else:
#                 print(heapq.heappop(양수힙))
#     ####################################################################
#         elif not 양수힙:
#             print(-heapq.heappop(음수힙))

#         else: # 둘다 있으면 이제 비교
#             음수 = -heapq.heappop(음수힙)
#             양수 = heapq.heappop(양수힙)

#             if abs(음수) > abs(양수):
#                 print(양수)
#                 heapq.heappush(음수힙, -음수)

#             else:
#                 print(음수)
#                 heapq.heappush(양수힙, 양수)

# import sys
# import heapq

# n = int(input())
# q = []

# for i in range(n):
#     a = int(input())
#     if a != 0:
#         heapq.heappush(q, (abs(a), a))
#     else:
#         if not q:
#             print(0)
#         else:
#             print(heapq.heappop(q)[1])
