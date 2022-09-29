import sys
input = sys.stdin.readline

n = int(input())
num_list = []

for _ in range(n):  #n만큼 반복
    num = int(input()) #n만큼 숫자 input
    num_list.append(num)  #list에 input값 넣기
#리스트를 정렬
num_list = sorted(num_list)    
#여기부터 구글링->각각의 값을 넣어야하는 건 알았지만 밖으로 빼내야 된다는 생각을 못함
#답은 각각의 값이 나와야 하므로
for i in num_list :  
    print(i)
    
#print(*li,sep='\n') for문 사용없이 개행으로만 할 수 있음