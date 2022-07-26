n, m = map(int, input().split())

common = []
great_common = 0
least_common = 0

for i in range(1, n + 1):
    for j in range(1, m + 1):
        if n % i == 0 and m % i == 0:
            common.append(i)

great_common += max(common)
print(great_common)
least_common += great_common * (n // great_common) * (m // great_common)
print(least_common)