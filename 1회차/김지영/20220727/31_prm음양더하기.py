absolute, signs = [4, 7, 12], [True, False, True]
# 절댓값을 담은 absolute
# sighns가 참이면 absolute는 양수, 아니면 음수
# absolute의 합
def solution(absolutes, signs):
    for i in range(len(absolutes)):
        if signs[i] == True:
            absolutes[i] = absolutes[i]
        else : absolutes[i] = -absolutes[i]
    return sum(absolutes)