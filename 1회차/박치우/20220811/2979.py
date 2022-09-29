import sys
sys.stdin = open('2979.txt')

A,B,C = map(int,input().split())
total_lst = []
min = 9999
max = -9999

for i in range(3):
    time = list(map(int,input().split()))
    total_lst.append(time)

for i in range(3):
    if total_lst[i][0] < min:
        min = total_lst[i][0]
    if total_lst[i][1] > max:
        max = total_lst[i][1]

lst = [[0] * max for _ in range(3)]
print(lst)
count = 0

for A,B in total_lst:
    lst[count][A:B] = 1
    count += 1

print(lst)



    



    



    
