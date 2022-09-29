def solution(absolutes, signs):
    answer = 123456789
    
    negative = 0
    for i in range(len(signs)):
        if not signs[i]:
            negative += absolutes[i]
            
    answer = sum(absolutes) - 2 * negative

    # 한 줄로 끝낸 풀이
    # return sum(absolutes if sign else -absolutes for absolutes, sign in zip(absolutes, signs))
    
    return answer