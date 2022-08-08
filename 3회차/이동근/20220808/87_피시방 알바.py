# from collections import Counter

# N = int(input())

# customer = input().split()

# print(sum(Counter(customer).values()) - len(set(customer)))
N = int(input())

customer = input().split()

print(len(customer) - len(set(customer)))