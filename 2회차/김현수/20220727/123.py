score_lst = []
for i in range(10):
    score_lst.append(int(input()))
result = score_lst[0]
if sum(score_lst) < 100:
    print(sum(score_lst))
else:
    for score in score_lst[1:]:
        b_result = result
        result += score
        if abs(b_result-100) > abs(result-100):
            pass
        elif abs(b_result-100) == abs(result-100):
            print(result)
            break
        elif abs(b_result-100) < abs(result-100):
            print(b_result)
            break

#현중님 - for~else문으로 해결!