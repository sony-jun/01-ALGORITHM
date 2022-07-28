N =int(input())
book_list = {}
best_list = []

for a in range(N) :
    book = input()
    book_list[book] = book_list.get(book , 0) + 1


for best in book_list :
    if book_list[best] == max(book_list.values()) :
        best_list.append(best)

best_list.sort()
print(best_list[0])