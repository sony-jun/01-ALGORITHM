import sys
sys.stdin = open('B1292.txt')

a, b = map(int, input().split())
num_list = [0] # 코드상으론 [0]부터 시작이니까 [1]이 1이 되게 0 넣어놓기
sum_ = 0

for i in range(1, b + 1): # b까지 수열 먼저 만들기 
    # print(i) 1 2 3 4 5 6 7 
    for j in range(i): # 1은 1번, 2는 2번,3은 3번... 반복
        num_list.append(i)
       # print(num_list)
       # [0, 1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 5, 6, 6, 6, 6, 6, 6, 7, 7, 7, 7, 7, 7, 7] 
for l in range(a, b + 1):
    sum_ += num_list[l]
    
print(sum_)

# print(sum(number[A-1:B]))