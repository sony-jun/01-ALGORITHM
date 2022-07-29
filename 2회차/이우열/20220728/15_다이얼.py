d = {
    'ABC': 2,
    'DEF': 3,
    'GHI': 4,
    'JKL': 5,
    'MNO': 6,
    'PQRS': 7,
    'TUV': 8,
    'WXYZ': 9
}

n = input()
sum_ = 0

d_k = list(d.keys())

for i in n:
    for j in range(len(d)):
        if i in d_k[j]:
            sum_ += d[d_k[j]] + 1

print(sum_)
