N, M = map(int, input().split()) # N장의 카드와 M의 숫자 

num = list(map(int, input().split())) 
sum = 0
for i in range(len(num)): # 첫번째 카드
    for j in range(i+1, N): # 그다음 카드
        for k in range(j+1, N): # 다다음 카드 
            # print("i :"+str(i))
            # print("j :"+str(j))
            # print("k :"+str(k))   

            # 카드 3장 합이 M보다 작거나 카드 3장 합이 sum보다 작으면 건너뜀          
            if num[i]+num[j]+num[k] > M or num[i]+num[j]+num[k] < sum:
                continue
            # 그외에는 합산
            sum = num[i]+num[j]+num[k]
print(sum)


