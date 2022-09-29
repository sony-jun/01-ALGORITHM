# 빈 리스트를 받아주고
M = []

# 리스트에 값을 추가해준다.
for i in range(int(input())):
    M.append(int(input()))


#for문 밖에서 정렬해주고 
k = sorted(M)
# 언팩킹
print(*k, sep="\n")

