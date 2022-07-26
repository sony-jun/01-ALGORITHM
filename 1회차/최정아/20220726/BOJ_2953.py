# 예제 입력은 contestant에 넣음
contestant = []
cont_sum = []
for a in range(5):
    # map함수 사용해서 contestant에 담음
    contestant.append(list(map(int, input().split())))
    # index에 따른 각 숫자들의 합을 구함
    cont_sum.append(sum(contestant[a]))
# 가장 큰 수의 index와 숫자 출력
print(cont_sum.index(max(cont_sum))+1, max(cont_sum))