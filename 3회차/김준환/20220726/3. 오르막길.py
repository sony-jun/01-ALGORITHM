# 측정 횟수 입력
# 수열 입력
# 횟수만큼 반복하며 수열 리스트 하나씩 꺼내서 이전 숫자와 감소면 길이 변수 초기화
# while 증가면 리스트에 숫자 두 개 계속 추가하여 while 끝나고 맨앞과 맨뒤 차이 리스트에 저장

n = int(input())
regit_lst = list(map(int,input().split()))
height_lst = []
height = 0
for i in range(n-1):
    if regit_lst[i] < regit_lst[i+1]:
        height += regit_lst[i+1]-regit_lst[i]
        i += 1
    else:
        height_lst.append(height)
        height = 0
    height_lst.append(height)
print(max(height_lst))