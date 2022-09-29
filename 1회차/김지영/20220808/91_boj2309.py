# 9개 중 2개 뽑는 경우의 수..
# 총합에서 2마리 빼면 100을 찾자.
# 20
# 7
# 23
# 19
# 10
# 15
# 25
# 8
# 13
tall = [int(input()) for _ in range(9)]
# print(tall)
sum_tall = sum(tall)
for i in range(8):
    for j in range(i+1,9):
        if sum_tall - tall[i] - tall[j] == 100:
            sub_i = tall[i]
            sub_j = tall[j]
            # print(sub_i,sub_j) # 15,25

tall = sorted(tall) # 정렬
tall.remove(sub_i) # 제거
tall.remove(sub_j)

for i in tall:
    print(i)
# 7
# 8
# 10
# 13
# 19
# 20
# 23