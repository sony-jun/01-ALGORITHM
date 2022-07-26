# 5번 반복하며 참가자 순서대로 각자 점수 합 구함
# 합이 가장 큰 참가자의 번호와 점수 출력
# 점수를 리스트로 받고 그 합을 점수 리스트에 순서대로 넣기
# 점수 리스트 인덱스로 참가자 번호 파악 가능
# max로 최대 점수 파악 후 .index로 참가자 번호 검색 및 출력

score_lst = []
for i in range(5):
    score_sum = sum(list(map(int, input().split())))
    score_lst.append(score_sum)
print(score_lst.index(max(score_lst))+1, max(score_lst))