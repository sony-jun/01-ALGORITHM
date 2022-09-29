import sys

sys.stdin = open("1157.txt")

# print(ord(alpha) # a = 97, A = 65, b = 98, B = 66 => 서로 32의 차이가 있음
# a = 97 ~ z =122, A = 65, Z = 90 => 알파벳은 25차이 있음

# alpha = ord(alpha) # 여기서 ord사용해서 int로 만들어주면 안될듯, len사용해야 하기때문

# print(alpha) # 97

# 대문자로 출력해야하니까 소문자가 입력되었을 때 32를 빼서 대문자로 만듬
# if alpha >= 97: # a입력
#     alpha -= 32
#     print(chr(alpha)) # A 출력

alpha = input()

list_ = [0] * 26 # 알파벳은 26개 # 0목록 만듬
# print(list_) # [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

max_alpha = 0
answer = 0

for i in range(len(alpha)):
    if ord(alpha[i]) >= 97: # ord안에선 int가 아니라 str이여야 함
        list_[ord(alpha[i]) - 97] += 1 # 소문자를 대문자로 바꾼것을 list_에 저장하고 for문 돌면서 리스트에 입력된 값을 저장시켜줌
        # -97 = -(32+65) : ord(A) = > 65
        # list_[0], list_[1], list_[2]...
    else:
        list_[ord(alpha[i])] += 1

max_alpha = max(list_) # max를 사용하여 list_의 최대값을 max_alpha 변수에 저장함

answer = list_.index(max_alpha) # answer : list_의 최대값의 인덱스 번호를 가짐

if list_.count(max(list_)) >= 2: # iiss와 같이 리스트 안에서 복수의 수가 있을 시 ? 출력
    print('?')
else:
    print(chr(answer + 65)) # 위에서 97을 빼줬기 때문에 다시 65을 더하고 chr 사용하여 문자로 표현함
# 백준에서 run time error 남


# alpha = input().upper() # 입력된 값을 대문자로 바꿔줌
# # print(alpha)
# set_alpha = set(alpha) # 중복이 일어나지 않게 set 사용, 어짜피 알파벳 1개만 나와야함
# list_alpha = list(set_alpha) # 중복 제거한 입력값을 리스트로 만듬
# # print(list_alpha)
# count = 0

# for i in list_alpha:



