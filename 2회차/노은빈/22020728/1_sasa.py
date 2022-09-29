n, m = map(int, input().split())
#n과 m input

#n과 m의 합이 4일때마다 sasa
# total = n + m
# print(total // )  다른 값에는 적용 x

total = min(n, m) #둘 중 작은 최솟값 출력
print(total//2)  #몫