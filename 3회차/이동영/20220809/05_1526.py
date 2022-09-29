from itertools import product
# import sys

# sys.stdin = open("input.txt", "r")
data = ['4','7']
n = int(input())
list_ = []

for i in range(1,7):
    result = []
    result = list(product(data, repeat = i))
    
    for j in result:
        list_.append(''.join(j))

for i in range(len(list_)):
    if n < int(list_[i]):
        print(list_[i-1])
        break
    if n == int(list_[i]):
        print(list_[i])
        break
    if n > int(list_[len(list_)-1]):
        print(list_[len(list_)-1])
        break