# input 저장할 리스트 선언
score = []
# 답 변수 0으로 초기화
ans = 0
# 반복 변수 0으로 초기화
k = 0

# 10번 순회
for i in range(10):
    # input 값 score 리스트에 추가
    score.append(int(input()))

# k가 9보다 크면 반복 끝
while k <= 9:
    # ans에 score 값 더하기
    ans += score[k]

    # ans가 100이 되면
    if(ans == 100):
        # 반복문 빠져나오기
        break

    # ans가 100보다 크면
    elif ans > 100:
        # 여태 더한 값에서 100 뺀 값이 
        # 여태 더한 값에서 맨 마지막 값 뺀 값을 100에서 뺀 값보다
        # 작거나 같으면
        if ans - 100 <= 100 - (ans - score[k]):
            # 반복문 빠져나오기
            break
        # if가 아니라면
        else:
            # ans에서 맨 마지막 값 빼기
            ans -= score[k]
        # 반복문 빠져나오기
        break
    
    # 반복 변수에 1 더하기
    k += 1

print(ans)