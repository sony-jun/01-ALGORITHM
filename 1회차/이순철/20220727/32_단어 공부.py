# https://www.acmicpc.net/problem/1157
a = list(map(ord, input()))
# print(a, type(a))
cnt = 0

for i in range(len(a)):
    # print(i)
    if (a[i] + 32) > 128:
        a[i] = a[i] - 32
# print(a, type(a))
A = list(map(chr, a))
# print(A, type(A))
for i in range(len(A)- 1):
    cnt.count(A[i])
print(cnt)