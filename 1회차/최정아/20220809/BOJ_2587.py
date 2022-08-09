x = []
for i in range(5):
    x.append(int(input()))
print(int(sum(x) / 5)) # 평균
x.sort() # 정렬
print(x[2]) # 중앙값