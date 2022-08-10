matrix = []

for i in range(20):
    i = int(input())
    matrix.append(i)

a = matrix[0: 10]
b = matrix[10::]

a.sort(reverse= True)
b.sort(reverse= True)

W = a[0] + a[1] + a[2]
K = b[0] + b[1] + b[2]
print(W, K)
# W = str(max(a[0] + a[1] + a[2]))
# K = str(max(b[0] + b[1] + b[2]))