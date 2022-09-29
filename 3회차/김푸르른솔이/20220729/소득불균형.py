T = int(input())

for _ in range(1, T + 1): #test case의 수를 정해준다.
    n = int(input())
    money = list(map(int,input().split())) #소득을 입력받아 리스트로 변환해준다.
    avg = sum(money)/n # 소득의 합을 구한뒤 사람수로 나누어 평균을 구해준다.
    cnt = 0 
    for i in money: 
        if i <= avg: # 소득이 평균보다 작을경우 +1을 해준다.
            cnt += 1
    print(f'#{_} {cnt}') # 소득의 평균보다 적게 버는 사람의 수를 확인한다.