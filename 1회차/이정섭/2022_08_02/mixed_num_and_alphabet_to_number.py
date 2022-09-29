s = input()

def solution(s):
    answer = s 
    dic_str = {'zero':0, 'one':1, 'two':2, 'three':3, 'four':4, 'five':5, 'six':6, 'seven':7, 'eight':8, 'nine':9}
    
    for item in dic_str.items():  
        answer = answer.replace(item[0], str(item[1]))   
    return int(answer)
# `dictionary.items()`
# The items() method returns a view object. 
# The view object contains the key-value pairs of the dictionary, as tuples in a list.
# The view object will reflect any changes done to the dictionary, see example below.`

print(solution(s))