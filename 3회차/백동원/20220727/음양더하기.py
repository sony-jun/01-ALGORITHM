def solution(absolutes, signs):
    result_list = []
    for i in range(len(absolutes)):                                 # absolutes의 길이 만큼 반복한다.
        if signs[i] == True:                                        # absolutes와 같은 위치의 signs 가 True 이라면
            result_list.append(absolutes[i])                        # 그대로 결과 리스트에 추가한다.
        else:                                                       # False 라면?
            result_list.append(absolutes[i] - (2 * absolutes[i]))   # 음수 값을 결과 리스트에 추가한다. 이 때 음수는 절대값에 절대값의 2배를 빼서 산출한다
    return sum(result_list)                                         # 모두 더한 값을 출력