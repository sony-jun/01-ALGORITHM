# https://school.programmers.co.kr/learn/courses/30/lessons/68644
def solution(numbers):
    new_list=[]
    value=0
    for i in range(len(numbers)-1):
        value += 1 
        for j in range(len(numbers)-(i+1)):
            new_num = numbers[i] + numbers[j+value]  
            new_list.append(new_num)
        
    new_list1 = sorted(set(new_list))
    return new_list1


print(solution([2, 1, 3, 4, 1]))
print(solution([5, 0, 2, 7]))
