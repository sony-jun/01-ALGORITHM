import sys
sys.stdin = open("20220726/2231_분해합.txt")

N = input()     # 주어진 분해합 N

for num in range(int(N)+1):     # 생성자 num
    num_list = list(map(int, str(num))) # num의 각 자리수 리스트

    de_num = num + sum(num_list)  # num의 분해합 = num + 각 자리수

    if de_num == int(N): # de_num이 N과 같다면 
        print(num)       # num이 생성자
        break
    if num == int(N):    # num을 1부터 N까지 확인했는데도 생성자가 없으면 
        print(0)         # 0을 출력