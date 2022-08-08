member = []
for _ in range(9):
    member.append(int(input()))
# 9명 중 2명을 뺀 값의 합이 100이면 일곱 난쟁이 발견!
# 9개 중  2개를 찾을 때  쓰는 범위 설정
for i in range(8):
    for j in range(i+1, 9):
        if sum(member) - (member[i]+member[j]) == 100:
            a, b = member[i], member[j]
# 2개를 제거하고 정렬
member.remove(a)
member.remove(b)
member.sort()
for i in range(7):
    print(member[i])