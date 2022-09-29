A, B, C = map(int, input().split())

l = []

for _ in range(3):
    a, b = map(int, input().split())
    l.append(set(range(a, b)))

total = 0

total += len(l[0] & l[1] & l[2]) * C * 3
total += (len(l[0] & l[1]) + len(l[0] & l[2]) + len(l[1] & l[2]) - (len(l[0] & l[1] & l[2]) * 3)) * B * 2
total += (len(l[0] - l[1] - l[2]) + len(l[1] - l[0] - l[2]) + len(l[2] - l[0] - l[1])) * A

print(total)


# 밑 코드가 더 낫다.
# https://www.acmicpc.net/source/47543221
# A, B, C = map(int, input().split())
# arr = [0] * 100
# result = 0

# for _ in range(3):
#     begin, end = map(int, input().split())
#     for i in range(begin, end): arr[i] += 1

# for j in arr:
#     result += {0 : 0, 1 : A, 2 : B * 2, 3 : C * 3}[j]
# print(result)