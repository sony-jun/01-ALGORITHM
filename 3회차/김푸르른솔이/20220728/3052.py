a = []

for _ in range(10):
    n = int(input())
    a.append(n%42)
a = set(a)
print(len(a))


# arr = []
# for i in range(10):
#     a = int(input())
#     if a%42 not in arr:
#         arr.append(a % 42)
# print(len(arr))\
# 이렇게도 가능