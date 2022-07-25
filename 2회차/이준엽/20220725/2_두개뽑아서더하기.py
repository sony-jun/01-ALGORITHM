# https://school.programmers.co.kr/learn/courses/30/lessons/68644
def solution(numbers):
    answerset = set()
    for i in range(len(numbers)):
        for j in range(i+1,len(numbers)):
                newnumber = numbers[i]+numbers[j]
                answerset.add(newnumber)
    answer = list(answerset)
    answer.sort() # 오름차순이라고 했으므로
    return answer

