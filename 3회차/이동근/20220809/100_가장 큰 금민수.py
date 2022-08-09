N = int(input())

check = "47"
ret = 0
flag = False

for i in range(4, N + 1):
    for num in str(i): 
        if num not in check:
            flag = True
            break

    if flag:
        flag = False
    else:
        ret = i

print(ret)

# 시간이 많이 차이 나서 살펴본 코드
# 1에서 시작하는게 아닌 N에서 감소하는 방식이라 신박하다.
# https://www.acmicpc.net/source/47424737

# N = int(input()) # N이 주어진다.
# while True: # 반복문 while 사용
#     count = 0

#     for i in str(N):
#         if i != '4' and i != '7': # 4나 7이 아니라면 count 해준다.
#             count = 1
#             N -= 1

#     if count == 0: # 4나 7로만 이루어져 있으면 출력
#         print(N)
#         break

# 위 코드보다 간결하고 내 처음 생각을 잘 구현한 코드.
# https://www.acmicpc.net/source/47424186
# n = int(input())
# for i in range(n,-1,-1):
#     if len(set(str(i)) - set(['4', '7'])) == 0:
#         print(i)
#         break