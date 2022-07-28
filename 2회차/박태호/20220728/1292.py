# 쉽게 푸는 문제
A, B = map(int, input().split())
# 3 7이면
# 1+2+2+3+3+3+4+4+.........
# 1 2 3 4 5 6 7
#     2 3 3 3 4 = 15 
#반복문으로 수열을 만들어야 하는데 
re = []
for i in range(1,B+1):# 수열먼저
    

    for j in range(i):
        re.append(i)
    #     re.append(j)
    #     print(re)
    #     print("----")
print(sum(re[A-1:B]))