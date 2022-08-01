T = int(input()) # 테스트 케이스 수

for i in range(T):
    a = list(input()) # 리스트를 입력받음
    j = 0 # 괄호 판별을 위한 변수 
    try:
        while len(a) != 0: # a의 길이가 0 이 될때까지 
            if a[j] + a[j+1] == "()": # j와 그다음 문자의 합이 ()면
                a.pop(j+1) # )를 빼냄
                a.pop(j) # (를 빼냄
                j = 0 # j 초기화
            elif a[j] + a[j+1] != "()": # 합이 ()가 아니라면?
                j += 1 # j를 증가시키면서 ()를 찾아냄
            if len(a) == 0: # 모든 값이 다 빠져나가면
                print("YES") # YES
                break    
    except IndexError: # 빠져나가지 못하고 IndexError발생시 
                print("NO") # NO
        