import sys
sys.stdin = open("2495.txt")

for _ in range(1):
    num = input()
    slice_num = []
    check_num = {}
 
    for i in num[0:]:
       slice_num.append(int(i))

    print(slice_num)
    for j in range(0, len(slice_num)-1):
        if j not in check_num: 
            check_num[slice_num[j]] = 1
        if slice_num[j] == slice_num[j+1]:
            check_num[slice_num[j]] += 1
                # if slice_num[-1] == slice_num[j]:
                #     check_num[slice_num[j]] += 1
            
        # if slice_num[j] == slice_num[j+1]:
        #     check_num[j] += 1
        # print(slice_num[j],slice_num[j+1])

    

    print(check_num)
    













    
    # # max_num = max(slice_num)
    # # cnt_num = slice_num.count(max_num)
    # print(slice_num)
    # cnt = 1
    # for j in range(0, len(slice_num)-1):
    #     if slice_num[j] == slice_num[j+1]:
    #         cnt += 1
    #     else:
    #         check_num[slice_num[j]] = cnt
    #         if slice_num[j] == slice_num[j-1]:
    #             check_num[slice_num[j]] = cnt
    #         cnt = 1
    #     print(cnt, slice_num[j])
    # print(check_num)
    # #     else:
    # #         if slice_num[j] == slice_num[j-1]:
    #             check_num.append(slice_num[j])
    #         if slice_num[-1] == slice_num[-2]:
    #             check_num.append(slice_num[-1])
    # print(cnt_num)
    # print(max_num)
    # print(cnt_num)
    
 
            

        



