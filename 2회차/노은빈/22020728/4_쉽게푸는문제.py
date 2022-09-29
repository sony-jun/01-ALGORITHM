a, b = map(int, input(). split())
lst = []
for i in range(b+1) :
    for j in range(i) :  #i만큼 반복  
        #i=1->j=0 // i=2 -> j=0,1 // i=3 -> j = 0,1,2
        if len(lst) == b :  #리스트의 개수가 마지막 숫자인 b일 때 멈추기
            break
        lst.append(i)  #빈 리스트에 1,2,2,3,3,3... 추가
    print(sum(lst[a-1:b]))  #인덱스가 0부터 시작이므로 a-1하기
    #a,b 가 3 7이면 인덱스가 2부터 6까지이므로(0~6)
