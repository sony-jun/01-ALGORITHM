import sys

sys.stdin = open("44_나머지.txt")

n_list = []


for i in range(1,11):
    n = int(input())
    n_list.append(n % 42)
n_list = set(n_list)    
print(len(n_list))
