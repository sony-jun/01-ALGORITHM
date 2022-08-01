
color = ['black', 'brown', 'red', 'orange', 'yellow', 'green', 'blue', 'violet', 'grey', 'white']
val = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
mul = [1, 10, 100, 1000, 10000, 100000, 1000000, 10000000, 100000000, 1000000000]

st = input()
nd = input()
rd = input()

res = 0 
for i in range(10):
    if color[i] == st:
        res += val[i] * 10
    if color[i] == nd:
        res += val[i] 

for j in range(10):
    if color[j] == rd:
        res *= mul[j]

print(res)
