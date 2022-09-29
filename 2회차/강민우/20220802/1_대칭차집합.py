N = input().split()
A = set(map(int, input().split()))
B = set(map(int, input().split()))
num1 = A-B
num2 = B-A

print(len(num1) + len(num2))
