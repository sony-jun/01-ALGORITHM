# 2693.
"""
"""
for i in range(int(input())):
    numbers = list(map(int, input().split()))
    numbers = sorted(numbers)
    max_numbers = numbers[-1:-4:-1]
    print(max_numbers[-1])