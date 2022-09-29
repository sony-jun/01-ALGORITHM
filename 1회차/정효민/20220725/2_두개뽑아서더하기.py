# https://school.programmers.co.kr/learn/courses/30/lessons/68644



def solution(numbers):
    # result1 = 0
    # list1 = 0
    # result2 = 0
    
    # answer = []
    # for i in numbers:
    #     answer.append(i)
    #     for z in answer:
    #         pass
    #     list1 = list1 + 1
    # for x in range(list1):
    #     answer[x]
    answer = list()
    for i in range(len(numbers)):
            for i2 in range(i + 1 , len(numbers)):
                sumnum = numbers[i] + numbers[i2] 
                if sumnum not in answer:
                    answer.append(sumnum)
    answer.sort()

        
        
        


            
    
        

    return answer
    

print(solution([2, 1, 3, 4, 1]))
print(solution([5, 0, 2, 7]))
