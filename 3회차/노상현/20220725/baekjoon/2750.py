# 수 정렬하기
# N개의 수가 주어졌을 때, 이를 오름차순으로 정렬하는 프로그램을 작성하시오.

n = int(input())
# 숫자를 담기위한 리스트 
li = [] 
for i in range(n):  #for 문을 이용하여 n개의 숫자들을 리스트에 담기 
    li.append(int(input())) # append 함수를 통해 입력된 값을 리스트 삽입
 
li.sort() # sort함수를 이용하여 오름차순으로 정렬
 
for i in li: # 정렬한 숫자들을 한개씩 출력
    print(i)