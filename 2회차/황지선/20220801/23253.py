# 23253번 자료구조는 정말 최고야

# 나머지 과목의 교과서 N권을 방 구석에 M개의 더미
# $N$권의 교과서는 각각 1부터 N까지의 번호가 매겨져 있다. 
# 찬우는 각 더미의 맨 위에 있는 교과서만 꺼낼 수 있으며, 
# 반드시 교과서를 꺼낸 순서대로 나열해야 하기 때문에 
# 번호순으로 나열하기 위해서는 1번, 2번, … N - 1번, N번 교과서 순으로 꺼내야 한다.
# 번호순으로 나열할 수 있는지 여부를 알려주는 프로그램을 작성해 주자.

# 첫째 줄에 교과서의 수 N, 교과서 더미의 수 M이 주어진다.
# 둘째 줄부터 2 x M줄에 걸쳐 각 더미의 정보가 주어진다.
# i번째 더미를 나타내는 첫 번째 줄에는 더미에 쌓인 교과서의 수 k_{i} 가 주어지며, 
# 두 번째 줄에는 k_{i} 개의 정수가 공백으로 구분되어 주어진다.
# 각 정수는 교과서의 번호를 나타내며, 아래에 있는 교과서의 번호부터 주어진다.
# 교과서의 번호는 1부터 N까지의 정수가 한 번씩만 등장한다.


from collections import deque


N, M = map(int,input().split())
dict = {}

for m in range(1, M+1):
    i = int(input())
    ki = deque(map(int, input().split()))
    ki.append(ki)
    dict[m] = ki

print(dict)

# 딕셔너리랑 융합하면 될까?


# n,m = map(int, input().split())
# y = list(range(1,n+1))
# list_di = []
# list_2 = []
# for i in range(m):
#     a = int(input())
#     list_number = list(map(int,input().split()))
#     for j in range(0,len(list_number)-1):
#         if list_number[j] < list_number[j+1]:
#             list_2.append(list_number[j+1])
        
            
# if list_2 == []:
#     print('Yes')
# else:
#     print('No')