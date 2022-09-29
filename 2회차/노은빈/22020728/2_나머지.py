div = []  #나눈 값을 넣을 빈 리스트

for i in range(10) : #10개의 숫자를 넣기 때문에 
    a = int(input())
    b = a % 42  # % : 나머지 구하는 연산자
    div.append(b) #리스트에 나머지 넣기

#중복값을 없앤 후 계산
set_div = set(div)
#서로 다른 나머지의 개수 구하기(len사용)
print(len(set_div))