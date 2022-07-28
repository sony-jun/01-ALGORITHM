


true = 0
false = 1
result = []

def solution(absolutes, signs):
    answer = 123456789
    result = []
    for i in range(len(absolutes)):
        if signs[i] == true:
            absolutes[i] = absolutes[i] * 1
            result.append(absolutes[i])
        #print(absolutes[i] , type[absolutes[i]])
        elif signs[i] == false:
            absolutes[i] = absolutes[i] * -1
            result.append(absolutes[i]) 
    answer = print(sum(result))
    return answer
   


        
    
    