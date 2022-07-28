# 두 수 입력으로 받기
a, b = map(int, input().split())

# 순열을 넣어주기 위한 리스트, 숫자에 해당하는 개수만큼 할당
su = []
for i in range(b + 1):
    for j in range(i):
        su.append(i)

# 구간에 속하는 숫자의 합 출력
print(sum(su[a-1:b]))