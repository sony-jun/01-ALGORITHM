def solution():
    answer = 0
    for _ in range(10):
        # 버섯 점수 확인
        score = int(input())
        # 버섯 점수 증가 
        answer += score
        # answer이 100 이상이면
        if answer >= 100:
            # (answer - score) = prev 
            prev, nxt = 100 - (answer - score), abs(answer - 100)
            if prev < nxt:
                answer -= score
                return answer
            elif nxt < prev or prev == nxt:
                return answer
    return answer

print(solution())