import sys
sys.stdin = open('일곱난쟁이_input.txt')

n = 9
height = [int(input()) for _ in range(n)]

total = sum(height) # 140

# 2개 더해서 40인걸 빼버리자
for x in range(n-1):
    for y in range(x+1, n):
        sum_ = 0
        sum_ += height[x] + height[y]
        if sum_ == total - 100:
            num1 = height[x]
            num2 = height[y]
            
height.remove(num1)
height.remove(num2)
height.sort()
for i in height:
    print(i)