n = int(input())
bestsell = {}
books = []
bs = []
for i in range(n):
    book = input()
    books.append(book)

for i in books:
    bestsell[i] = 0

for i in books:
    bestsell[i] += 1

for k, v in bestsell.items():
    if v == max(list(bestsell.values())):
        bs.append(k)
bs.sort()
print(bs[0])