t = int(input())
numList = []
for i in range(t):
    num = int(input())
    numList.append(num)

num_count = {}
for num in numList:
    num_count[num] = 0 # 특정 문자 딕셔너리에 추가
for num in numList:
    num_count[num] = num_count[num] + 1 # 추가한 딕셔너리에서 갯수 더하기

print(max(num_count,key=num_count.get))