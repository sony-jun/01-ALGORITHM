# numList = list(map(int,input().split('\n')))
numList = []
for i in range(10):
    numList.append(int(input()))
numList = list(numList)

splitNumList = []

#splitNumList에 numList의 숫자를 하나씩 꺼내서 42로 나눈 나머지의 값을 넣음
for i in numList:
    splitNumList.append(int(i%42))

num_count = {}
for num in splitNumList:
    num_count[num] = 0 # 특정 문자 딕셔너리에 추가
for num in splitNumList:
    num_count[num] = num_count[num] + 1 # 추가한 딕셔너리에서 갯수 더하기

#키 갯수 구하기
print(len(num_count))