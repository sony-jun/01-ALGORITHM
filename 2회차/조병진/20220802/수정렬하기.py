# 수 정렬하기
# 문제 : N개의 수가 주어졌을 때, 이를 오름차순으로 정렬하는 프로그램을 작성하시오.

n = int(input())

arr = []
for _ in range(n):
    num = int(input())
    arr.append(num)

sort_ = sorted(arr)

for i in sort_:
    print(i)
