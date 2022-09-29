import sys

sys.stdin = open("프로그래머스_음양더하기.txt")

def solution(absolutes, signs): 
    for i in range(len(absolutes)):
        if signs[i] == 'True':
            answer += absolutes[i]
        else:
            answer -= absolutes[i]
    return answer

