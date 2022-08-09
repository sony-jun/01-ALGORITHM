import sys
input = sys.stdin.readline

heights = [] # 난쟁이들의 키
for i in range(9):
    heights.append(int(input()))
heights.sort() # 오름차순으로 키를 정렬
whole_sum = sum(heights) # 키의 합
# 아홉 난쟁이의 키 - 가짜 난쟁이 둘의 키 = 100
for i in range(8): # i가 일곱 난쟁이 중 하나일 때 
    for j in range(i+1, 9): # j는 i 다음 인덱스부터 끝까지
        if whole_sum - (heights[i] + heights[j]) == 100:
            fake1, fake2 = heights[i], heights[j]
heights.remove(fake1)
heights.remove(fake2)

for answer in heights:
    print(answer)