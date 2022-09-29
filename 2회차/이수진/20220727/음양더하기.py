def solution(absolutes, signs):
    true=True
    false=False
    for i in range(len(signs)):
        if signs[i] == False :
            absolutes[i]=0-absolutes[i]
    answer = sum(absolutes)
    return answer