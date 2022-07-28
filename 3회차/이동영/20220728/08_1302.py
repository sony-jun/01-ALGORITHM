import sys

sys.stdin = open("input.txt", "r")

N = int(input())
book_list = []
new_book_list = []
dict = {}

for i in range(1,N+1):
    book_list.append(input())

for i in book_list:
    if i in dict:
        dict[i] += 1
    else:
        dict[i] = 1

for i in dict:
    if dict.get(i) == dict[max(dict, key=dict.get)]:
        new_book_list.append(i)

print(sorted(new_book_list)[0])