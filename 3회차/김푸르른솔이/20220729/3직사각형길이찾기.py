T = int(input()) 

for _ in range(1, T+1): # test case를 입력해준다.
    num = list(map(int, input().split())) # 길이를 리스트로 변환해준다
    num.sort() #작은수부터 정렬해준다.
    if num[0] == num[1]:
        print(num[2]) # 차례로 1, 2번째 숫자가 같으면 세번째 숫자를 출력하고
    else:
        print(num[0]) # 1, 2번째 숫자가 다르다면 첫번째 위치이 숫자를 출력한다.



