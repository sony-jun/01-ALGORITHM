def solution(absolutes, signs):
    sum=0
    idx=0
    for i in signs:
        k=absolutes[idx]
        if i:
            sum+=k
        else:
            sum-=k   
        idx+=1
    answer=sum 
    return answer