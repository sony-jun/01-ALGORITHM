for _ in range(3) :
    nums = input()

    cnt = 1
    cnt_sum = []
        
    for i in range(7) :

        if nums[i+1] == nums[i] :
            cnt += 1
            cnt_sum.append(cnt)
        
        else :
            cnt = 1

    if cnt_sum == [] :
        print(1)
    
    else :
        print(max(cnt_sum))
    