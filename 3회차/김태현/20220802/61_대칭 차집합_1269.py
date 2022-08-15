import sys
sys.stdin = open("61_대칭 차집합_1269.txt", "r")

# - 대칭 차집합 = 합집합 - 교집합
# - set(A+B 리스트)길이 - (A 리스트 길이 + B 리스트 길이 - set(A+B 리스트) 길이)

A, B = map(int, input().split())

two_lst = []
for _ in range(2):
    two_lst += list(map(int, input().split())) #[1, 2, 4, 2, 3, 4, 5, 6]

result = len(set(two_lst)) - (len(two_lst) - len(set(two_lst)))
print(result)