import sys
sys.stdin = open('B2309.txt')

heights = [int(input()) for _ in range(9)]
# print(heights)
total = sum(heights)
for i in range(9):
    for j in range(i+1, 9):
        if total - heights[i] - heights[j] == 100:
            fake1, fake2 = heights[i], heights[j]
            break
             
list.remove(fake1)
list.remove(fake2)
heights.sort()
print(heights, end='/n')