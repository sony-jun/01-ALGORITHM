A, B = map(int, input().split())


#입력값이 list에 담긴다
a_list = list(map(int, input().split())) 
#list에서 set으로 변환
a_set = set(a_list) 

#입력값이 list에 담긴다 #다른 분들 보니까 저처럼 list를 안 씌우고 set을 바로 씌웠네요... 그게 가능한지 처음 알았습니다...
b_list = list(map(int, input().split()))
#list에서 set으로 변환 
b_set = set(b_list) 


#대칭 차집합 구하기
difference = (a_set - b_set) ^ (b_set - a_set) 
#길이 출력
print(len(difference)) 

