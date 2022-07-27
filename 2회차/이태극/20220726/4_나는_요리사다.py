sum_list=[]
for i in range(5):
    a,b,c,d=map(int,input().split())   
    sum_list.append(a+b+c+d)
#입력받은 리스트 전체 출력
print("sum_list:",sum_list)
#리스트에서 가장 큰값 찾기
tmp=max(sum_list)
print("max:",tmp)
#큰값에 해당하는 인덱스 출력
index = sum_list.index(tmp)
print("index:",index)    
#정답
print(index+1, max(sum_list))
#인덱스는 0부터니 +1
# 5 4 4 5
# 5 4 4 4
# 5 5 4 4
# 5 5 5 4
# 4 4 4 5