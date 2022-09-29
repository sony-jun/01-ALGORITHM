#입력한 숫자들을 리스트화 시킨 다음
#sorted함수로 리스트를 정렬시켜준다.
#정렬된 리스트 내의 숫자들을 하나씩 출력시킨다.

n = int(input())
list = []

for _ in range(1, n+1):
    number = int(input())
    list.append(number)
list_sort = sorted(list)
for i in range(len(list_sort)):
    print(list_sort[i])
    
# 백준에서는 오답처리하지만
# pop을 활용해서 같은 결과가 나온 경우

n = int(input())
list = []

for _ in range(1, n+1):
    number = int(input())
    list.append(number)
while len(list):
    print(list.pop())