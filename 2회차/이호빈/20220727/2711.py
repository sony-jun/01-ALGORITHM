n = int(input())
for tc in range(1, n + 1):
    num, str = input().split()
    num = int(num)
    left = str[0:num-1] #0번째 인덱스부터 num-1까지 잘라주고
    right = str[num::] #num 이후 값 출력
    print(left+right) #그리고 더해준다
