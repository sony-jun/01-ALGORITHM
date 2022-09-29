
a, b = map(int, input().split())


min_ = min(a, b)              # 두 개의 수를 비교해서 큰 값과 작은 값을 나누고 진행하는 것이 편할것 같다고 생각함. 
max_ = max(a, b)
for i in range(min_, 0, -1) :     # 최대 공약수이므로, i를 큰 수부터 대입함. 
    if max_ % i == 0 and min_ % i == 0 :   ## 두 수 모두 i로 나누어 떨어진다면 공약수 성립
        print(i)
        break


    #?  print(a*b / i) 를 하면 바로 최대 공약수를 출력할 수 있다. 
    #? 그리고 min, max 할 필요 없을 것 같다. 
for i in range(1, max_+1) :      ## 최소 공배수를 구할때는 i를 1부터 차례로 곱해가는게 좋을 것 같다고 생각함. 
    if i * min_ % max_ == 0:    ## 공배수이므로, 큰 값으로 나누어 떨어져야 함. 
        print(i*min_)
        break


    ### 최대 공약수는 