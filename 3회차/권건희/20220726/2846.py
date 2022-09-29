
# 못풀어서 다른분꺼 참조해서 겨우품..
# 계단처럼 생각해서 차이를 더해나가고
# 중간에 오르막이 아니면 더해놨던 것들을 다른 곳에 옮겨놓고(차후에 비교해야 하기에 list로)높이를 리셋하고 
# 다시 오르막길을 더해나간다. 내리막or 평평 없이끝까지 가면 전부 더 해주는 거 만들어 두기.  
T=int(input())
list_=list(map(int,(input()).split()))
cnt=0
list_2=[]
for i in range(T-1):
    if list_[i+1]-list_[i]>0:
        cnt+=list_[i+1]-list_[i]
        
    if list_[i+1]-list_[i]<=0:
        list_2.append(cnt)
        
        cnt=0

    if i== T-2:
        list_2.append(cnt)

        
print(max(list_2))            