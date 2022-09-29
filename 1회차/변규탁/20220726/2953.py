score_list = []
for i in range(5):
    score_list.append(sum(list(map(int, input().split()))))

print("{} {}".format(score_list.index(max(score_list))+1,max(score_list)))
    

# 뭔가 한번에 우겨넣은 느낌인데 문제의 의도에 맞는지는 모르겠습니다.