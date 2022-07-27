def solution(absolutes, signs):
    for i in range (len(absolutes)): #absolutes가 입력된 숫자개수만큼 실행
        # print(absolutes)
        # print(len(absolutes))
        if signs[i] == False: # sings가 False면 absolutes의 리스트의 값에서 음수를 붙여줌
            absolutes[i] = -absolutes[i]
            # print(absolutes)
    return sum(absolutes) # absolutes의 맨 마지막의 리스트들을 더해준 것을 반환


print(solution([4, 7, 12], [True, False, True]))
print(solution([1, 2, 3], [False, False, True]))

# [4, 7, 12]
# [4, 7, 12]
# [4, -7, 12] 이게 출력되야 함
# 9
# [1, 2, 3]
# [-1, 2, 3]
# [-1, -2, 3] 이거
# 0