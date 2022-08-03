# n개의 수가 주어졌을 떄, 오름차순으로 정렬하는 프로그램

t = int(input())

list1 = []

for _ in range(t):
    list1.append(int(input()))

list1 = sorted(list1)

for i in range(len(list1)) : 
    print(list1[i]) #순서대로 끄내기 



# 방법2

t = int(input())

list1 = set()

for i in range(t):
    list1.add(int(input()))

list1 = list(list1)

list.sort()

for i in range(len(list1)):
    print(list1[i])