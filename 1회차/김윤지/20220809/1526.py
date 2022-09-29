n = int(input())

while True:
    cnt = False
    for i in str(n):
        if i != '4' and i != '7': # 4 와 7이 아니면
            cnt = True      # 참이니까
            n -= 1          # n에서 4와 7이 나올때까지 빼주기
           
    if cnt == 0: # 0이라면
        print(n) # n출력
        break

        