import sys
input = sys.stdin.readline

height = []
sum_ = 0

for i in range(9): #9명의 난쟁이 수만큼
    height.append(int(input()))  #난쟁이 키들을 input 받기
    sum_ += height[i]  #키 데이터들 더하기


for i in range(len(height)):
    for j in range(i+1, len(height)):
        if sum_ - (height[i] + height[j]) == 100: #전체 키들의 합에서 i와 j의 값을 뺀 게 100이면
            p1, p2 = height[i], height[j] #해당값
            break

height.remove(p1)  #해당값들을 지우기
height.remove(p2)
height.sort()  #키들 오름차순으로 정렬

for i in height :
    print(i)

