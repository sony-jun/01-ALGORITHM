n = int(input())
for i in range(1,n):                        # i 는 1부터 n까지의 반복문 
    num_list = list(map(int,str(i)))        # num_list 는 각 숫자의 자릿수를 문자열로 변환후 다시 정수형으로 저장.
    if i + sum(num_list) == n:              # 각 자릿수를 요소로 가지고 있는 리스트의 합과 i 를 더해 처음 입력값이 나오면 출력후 종료.
        print(i)
        break
else: 
    print(0)   