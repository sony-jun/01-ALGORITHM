def solution(absolutes, signs):
    # 답 변수 0으로 초기화
    answer = 0

    # signs 길이만큼 순회
    for i in range(len(signs)):
        # 만약 signs이 true면
        if signs[i]:
            # answer에 absolutes 값을 더함
            answer += absolutes[i]
        # 만약 signs이 false면
        else:
            # answer에 absolutes 값을 뺌
            answer -= absolutes[i]

    return answer