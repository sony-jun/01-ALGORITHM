result = []  

for i in range(5):
    score = list(map(int, input().split()))  #input을 숫자 리스트로
    result.append(sum(score))  #result 리스트에 더한 합계인 score 추가

print(result.index(max(result))+1, max(result))
#max(result)+1 == 인덱스 값이 0부터 시작이므로 참가자 번호는 +1 해야함