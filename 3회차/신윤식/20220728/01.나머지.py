# https://www.acmicpc.net/problem/3052

lst = [] # 나머지를 담을 리스트 생성

for i in range(10): # 10번 입력을 받아야함으로 인덱스 범위 10으로 설정
    number = int(input())
    lst.append(number % 42) # 나머지를 연산하여 리스트에 담아줌

deduplicate = list(set(lst)) # set을 이용하여 리스트안에 있는 중복값을 제거해줌

print(len(deduplicate)) # len을 이용하여 리스트안에 있는 요소 갯수를 세어줌