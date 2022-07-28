import sys
sys.stdin = open('3052.txt')

num_list = []

for i in range(10):
    numbers = int(input())
    num = numbers%42

    if num not in num_list: 
        num_list.append(num)

print(len(num_list))