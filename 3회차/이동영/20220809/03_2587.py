import sys

sys.stdin = open("input.txt", "r")

list_ = []
for _ in range(5):
    list_.append(int(input()))


temp = sorted(list_)

print(sum(list_)//5)
print(temp[2])