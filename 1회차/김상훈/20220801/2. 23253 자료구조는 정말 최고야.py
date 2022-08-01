import sys
sys.stdin = open("책더미.txt", "r") 

a , b = map(int,input().split())  #책 갯수 : 5 책 더미 갯수 2
result = ''

for j in range(b): 
    # 책더미 갯수 순회 (책더미 2개) 
    x = int(input()) 
    # 책더미의 높이 
    
    y = list(map(int,input().split())) 
    # 책 더미 높이만큼 리스트에 숫자 입력받기 (3,1)
    z = sorted(y, reverse=True) 
    # 리스트를 내림차순으로 정렬해서 z에 저장
    
    if y == z :
        result = 'Yes'
    else :
        result = 'No'
        
    if result == 'No':
        break
    
print(result)

#5 2
#3
#3 5 1
#2
#4 2