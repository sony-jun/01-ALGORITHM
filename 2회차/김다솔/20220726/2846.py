# https://www.acmicpc.net/problem/2846
import sys
sys.stdin = open('2846.txt', 'r')

n = int(input())
height = list(map(int, input().split()))
uphill = []
gap = 0

for i in range(n - 1):
    
    if height[i] < height[i + 1]:
        gap += height[i + 1] - height[i]
        
    if height[i] >= height[i + 1]:
        uphill.append(gap)
        gap = 0
        
uphill.append(gap)        
print(max(uphill)) 
