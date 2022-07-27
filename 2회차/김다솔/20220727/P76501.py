# https://school.programmers.co.kr/learn/courses/30/lessons/76501?language=python3

def solution(absolutes, signs):
# absolutes = [4,7,12]
# signs = [True, False, True]
    answer = 0
    for i in range(len(absolutes)): #인덱스 이용할거라 요소 개수만큼 range
        # print(i)
        if signs[i]:
            answer += absolutes[i]
        # if signs[i] == True: # 트루면 더하고 
        # elif signs[i] == False: # 폴스면 굳이 부호 바꾸고 그런거 하지말고 바로 빼기
        else:
            answer -= absolutes[i]
        
        return answer

print(solution([4,7,12], [True, False, True]))
