A, B = map(int, input().split())

l = []
# for i in range(1, 1001):

# 해당 코드가 가능한 이유는
# 수열의 개수는 1 + 2 + 3 + 4 + ... 순으로 증가하기 때문에
# 인덱스가 최대 1000 이므로  1 ~ 45까지의 총합은 1035이기 때문에
# 45까지범위를 설정하면 된다.
for i in range(1, 46):
    for j in range(i):
        l.append(i)

print(sum(l[A - 1: B]))