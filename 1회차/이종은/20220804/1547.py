# 공

t = int(input())

list1 = [1, 0, 0] # 첫번째 인덱스에 공이 있음을 의미하는 1을 할당하고 나머지 인덱스 값은 0으로 할당

for _ in range(t):
    x, y = map(int, input())
    list1[x-1], list1[y-1] = list1[y-1], list1[x-1] # 각 인덱스에 있는 값을 바꾸어줌, 여기서 인덱스 값은 입력 값-1이므로, -1해줌

for i in range(3):
    if list1[i] == 1: # 만약 0~2 인덱스 값 중, 1이 있는 것이라면 
        print(i+1) # 인덱스에 1을 추가해서 출력 
