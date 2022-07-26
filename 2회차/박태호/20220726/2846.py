n = int(input()) # 5
a = list(map(int, input().split())) # 1 2 1 4 6

dif = 0
high = [0]
for i in range(1,n):
    if a[i] > a[i-1] :           # a[1] > a[0] 으로 시작,뒤에 값이 더 크면 
        dif += (a[i]-a[i-1])     # 차이 변수에 증가시킴 
        high.append(dif)         # 리스트로 높이를 기록해둠 [1]  [1,3] [1,3,5]

    elif a[i] == a[i-1]: #평지면 차이는 없다.
        dif = 0     

    elif a[i] < a[i-1]: #오르막이 아니거나 끝나면
        dif = 0          #차이는 초기화함
print(max(high))
    

