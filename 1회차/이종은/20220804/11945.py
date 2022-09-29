# 뜨거운 붕어빵

a, b = map(int, input().split())

bbang = []

for i in range(a):
    # data = input()
    # print(data[::-1])
    bbang.append(input()) # 한줄마다 입력

for row in bbang:
    print(row[::-1])
        