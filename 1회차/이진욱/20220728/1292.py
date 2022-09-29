
A,B=map(int,input().split())

N_list = [  ] # 빈 리스트

for i in range(1,B+1): # 원소 숫자, 1부터 B까지 넣을거라 1,B+1 범위 설정

    for _ in range(i): # 원소의 반복 횟수
        N_list.append(i)

print(sum(N_list[A-1:B])) # A번째부터 B번째까지 