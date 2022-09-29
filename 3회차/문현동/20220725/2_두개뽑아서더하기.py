# https://school.programmers.co.kr/learn/courses/30/lessons/68644
def solution(numbers):
    
    answer = []
    
    for i in range(len(numbers)): # 리스트를 받아온다. i == 0 ~ 4
        numbers_pop = list(numbers) # 팝을 위한 리스트를 따로 만듦. 왜냐하면 팝을 하게되면 그 리스트에서 팝을 한 값이 사라지기 때문에 정상적인 계산이 안된다.
        ele = numbers_pop.pop(i) # 팝을 해온 값을 엘레멘트라는 변수에 따로 넣는다.
        for j in numbers_pop: # 그것이 빠진 리스트에 대하여 for 문 실행한다.
            answer.append(ele + j) # 정답 리스트에 numbers_pop 리스트의 처음 원소부터 끝 원소까지 각각 pop 원소와 더한다음 정답리스트에 추가한다.
            
    answer = sorted(list(set(answer))) # 정답리스트에서 중복을 없앤다음 리스트로 만들고 정렬한다.
    
    return answer # 반환한다.

print(solution([2, 1, 3, 4, 1]))
print(solution([5, 0, 2, 7]))

# set 에다가 계속 담은다음에 list.sort 해서 제출