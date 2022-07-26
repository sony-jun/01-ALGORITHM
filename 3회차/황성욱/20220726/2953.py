li = [] # 점수를 담기 위한 빈 리스트 생성
for i in range(5): # 5번의 입력을 받아
    score = sum(list(map(int, input().split()))) # list로 받은 값을 합하여 score 변수에 저장
    li.append(score) # 리스트에 추가

print(li.index(max(li)) + 1, max(li)) # max와 index 함수를 이용하여 원하는 값 출력