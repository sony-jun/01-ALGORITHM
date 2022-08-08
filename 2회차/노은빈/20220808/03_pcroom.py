# import sys
# input = sys.stdin.readline

# n = int(input())
# num = list(map(int,input().split()))
# cnt = 0  #거절당하는 사람 수

# for i in range(n-1):
    
#     if num[i] == num[i+1]:
#         cnt += 1
#     else :
#         cnt = 0

#print(cnt)

#다른 사람 코드
n = int(input())
list_ = []  #이미 차 있는 자리
num = input().split()
cnt = 0  #거절당하는 사람 수

for i in range(n):
    
    if num[i] not in list_: #빈 리스트에 input값이 없다면
        list_.append(num[i])  #리스트에 추가      
    else :
        cnt += 1  #있다면 +1

print(cnt)



