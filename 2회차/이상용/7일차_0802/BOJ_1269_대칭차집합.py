n, m = map(int, input().split())
a = set(map(int, input().split()))
b = set(map(int, input().split()))

print(len(a ^ b))
# print(len(a-b) + len(b-a))도 가능