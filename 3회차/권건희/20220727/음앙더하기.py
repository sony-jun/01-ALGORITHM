
def solution(absolutes, signs):

    for i in range(len(absolutes)):
        print(absolutes[i])
        if absolutes[i] and signs[i]==False:
            absolutes[i]=-int(absolutes[i])
        else: absolutes[i]=int(absolutes[i])    

    

    answer = sum(absolutes)
    return answer