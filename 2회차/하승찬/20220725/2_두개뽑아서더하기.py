# # https://school.programmers.co.kr/learn/courses/30/lessons/68644
def solution(numbers):
    answer = []
    for i in range(len(numbers)): # 리스트의 갯수 확인
        for idx in numbers[i:i+1]: # 리스트의 인덱스 값을 하나씩 가져옴
         for listn in numbers:
            answer.append(idx+listn) 
        answer.remove(idx+idx)
    
    return sorted(list(set(answer)))

# # 정수 배열 numbers가 주어집니다. numbers에서 서로 다른 인덱스에 있는 두 개의 수를 
# # 뽑아 더해서 만들 수 있는 모든 수를 배열에 오름차순으로 담아 return 하도록 solution 함수를 완성해주세요.
# numbers= [5, 0, 2, 7]

# answer =[]

# # # 넘버스 리스트를 for문을 두번 중첩해서 돌리고 두번째 for문에서는 인덱스 n의 값을 지웠다가 끝나고나서 다시 넣어준다.
# for i in range(len(numbers)): # 리스트의 갯수 확인
#    for idx in numbers[i:i+1]: # 리스트의 인덱스 값을 하나씩 가져옴
#     for listn in numbers:
#         answer.append(idx+listn) 
#     answer.remove(idx+idx)

# re= list(set(answer))
# print(re)

# # for문을 중첩해서 한 원소당 다음 리스트가 모두 순환되어 더한값을 set을 통해 리스트로 정렬한 후 출력 
# print(solution([2, 1, 3, 4, 1]))
# print(solution([5, 0, 2, 7]))
# solution1= [2, 1, 3, 4, 1] # 문제 잘못이해

# solution2= [5, 0, 2, 7]

# n_sum= set()

# for n1 in solution1:
#     for n2 in solution2:
#         n_sum.add(n1+n2)

# print(n_sum)