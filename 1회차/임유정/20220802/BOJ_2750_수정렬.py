# N개의 수가 주어졌을 때, 이를 오름차순으로 정렬하는 프로그램을 작성하시오.

T = int(input())
num_list = [] #숫자들의 리스트 열어줌

for i in range(T): 
    num_list.append(int(input())) # T만큼 반복해서 num_list에 항목추가
num_list1 = sorted(num_list) # sorted를 이용하여 정렬 sort>기본오름차순
for i in range(len(num_list)): # len 이용하여 길이 구해 반복항목 확인
    print(num_list1[i]) #요소 하나씩 출력
