# x : 몸무게, y : 키

N = int(input())

d_list = []

for i in range(N):
    d_list.append(list(map(int, input().split())))
    
for d in d_list:
    check = 1
    for c in d_list:
        if d[0] < c[0] and d[1] < c[1]:
            check +=1
    print(check, end=" ")
