n = int(input())
num_list = list(map(int,input().split()))
cnt = 0     # 오르막길을 수치화해 저장할 변수 선언. 
cnt_list=[]    # 각 오르막길별로 오르막 차이를 저장할 리스트
for i in range(n-1):
    if num_list[i] < num_list[i+1]: # i에서부터 연속하는 순서가 오름차순일때 
        cnt += num_list[i+1]-num_list[i] # cnt에 오르막 차이를 저장.
    else:    # 내림차순일때는 cnt 초기화 
        cnt=0
    cnt_list.append(cnt)
print(cnt_list)
print(max(cnt_list))
