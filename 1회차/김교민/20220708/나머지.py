A_list = []
for i in range(10):
    A = int(input())
    A_list.append(A%42) #입력받은 A값에 42를 나눈 나머지를 넣어둔다.

A_list=set(A_list) #리스트를 set로 집합 자료형으로 변환한다.
print(len(A_list)) # 마지막으로 set시킨 A_list의 길이를 출력한다.