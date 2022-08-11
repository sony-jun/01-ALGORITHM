a = int(input()) # input 값 받기용
lis = list(map(int, input().split())) # 카드 10장 list 만들기
dic = {} # 빈 dic 변수
for i in lis: # lis 반복
    if i in dic: # lis 각 값이 dic에 있다면
        dic[i] += 1 # key i 값에 + 1
    else: # 아니라면
        dic[i] = 1 # key i = 1 생성
        
b = int(input()) # input 값 받기용
lis2 = list(map(int, input().split())) # 카드 8장 list 만들기

result = [] # 결과 변수
for i in lis2: # lis2 반복
    if i in dic: # lis2 각 값이 dic에 있다면
        result.append(dic.get(i)) # 변수에 추가 한다 dic 안에 i의 key를
    else: # 아니라면
        result.append(0) # 변수에 0 추가

print(*result) # 결과 값 프린트