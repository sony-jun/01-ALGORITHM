result=[] #빈 list 생성

for i in range(5): # for문을 5번 돌면서
    
    # 각각의 리스트에 정수형 값을 sum 함수로 더한 후 result 리스트에 넣는다.
    result.append(sum(map(int,input().split()))) 

print(result.index(max(result))+1,max(result)) 
# result의 최댓값을 가지는 인덱스와 번호와 최댓값을 출력한다,.

