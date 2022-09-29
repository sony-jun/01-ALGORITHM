import sys
sys.stdin = open('대표값2_input.txt')

n = 5
number = []
for i in range(n):
    num = int(input())
    number.append(num)
avg_ = sum(number) / n
print(int(avg_))
number.sort()
for i in range(n):
    if i == round(len(number)/2):
        print(number[i])
