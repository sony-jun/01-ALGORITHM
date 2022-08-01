t = int(input())

for _ in range(t): # 3번 반복
    check = input() # ((넣기 
    ls = list(check) # 리스트로 형변환 
    sum = 0 # 카운트 셋팅

    for i in ls: # 두번 반복 
        if i == "(": 
            sum += 1 # 1해주고 
        elif i == ")": 
            sum -= 1
        if sum < 0: #0보다 커서 다시 위 포문으로 가서 1해줘서 2되고 
            print("NO")
            break
    if sum > 0: #2번 반복하고 이쪽으로 내려와서 2가 0보다 크니깐 no 
        print("NO")
    elif sum == 0:
        print("YES") 