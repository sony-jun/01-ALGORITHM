import sys
sys.stdin = open("1292_쉽게푸는문제.txt")

# 리스트를 만들어서 for문 사용하는게 좋지 않을까?
list_ = []

F, S = map(int, input().split()) # F: First, S: Second

for i in range(1, S+1): # 뒤에 입력되는 값이 무조건 큼
    list_.append(i)
# print(list_) # [1, 2, 3, 4, 5, 6, 7] 만듬

for j in range(S):
    print(list_)

# 못풀었음 ㅠ