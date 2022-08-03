n = int(input())
books = {}

for _ in range(n) :
    book = input()
    if book not in books :
        books[book] = 1
    else :
        books[book] += 1


# a = {v, k for k, v in books.items()}
books_re = dict(zip(books.values(), books.keys()))
best_seller = max(books_re)

print(books_re[best_seller])

# 정답 코드
import sys
book = dict()
n = int(input())
for _ in range(n):
    name = sys.stdin.readline().rstrip()
    if name in book:
        book[name] += 1
    else:
        book[name] = 1
max = 0
sbook = dict(sorted(book.items()))
for i in sbook:
    if (sbook[i]) > max:
        max = sbook[i]
        maxi = i
print(maxi)
