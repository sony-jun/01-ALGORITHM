mush_lst = []
for i in range(10):
    n = int(input())
    mush_lst.append(n)
mush_sum = 0
for i in range(len(mush_lst)):
    mush_sum += mush_lst[i]
    if mush_sum == 100:
        answer = mush_sum
        break
    elif mush_sum > 100:
        if mush_sum - 100 > 100 - (mush_sum-mush_lst[i]):
            answer = mush_sum-mush_lst[i]
            break
        else:
            answer = mush_sum
            break 
    elif mush_sum < 100 and i == len(mush_lst)-1:
        answer = mush_sum
print(answer)