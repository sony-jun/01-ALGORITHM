total = []
for i in range(5):
    #참가자 별 점수 받는 동시에 점수 합을 total 리스트에 추가
    total.append(sum(map(int, input().split())))

#total중 최댓값의 인덱스+1로 참가자 번호 출력하고 최대값으로 점수 출력
print(total.index(max(total))+1, max(total))