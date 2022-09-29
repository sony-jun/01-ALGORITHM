# https://school.programmers.co.kr/learn/courses/30/lessons/68644
ans = set()

def solution(numbers):
    for i in range(len(numbers)):
        for j in range(len(numbers)):
            if j != i:           # number를 순회하도록 하니까 리스트에 1,1 이런식으로 서로다른 1이 있을때 두개가 합해지지않음 !!! 
                ans.add(numbers[j] + numbers[i])      # 그래서 단순 숫자가 아닌 리스트의 구성요소를 더하게 했음
    answer = sorted(list(ans))

    return answer


print(solution([5, 0, 2, 7]))  # 테스트케이스중 2개가 틀렸다고나오는데 확인이 불가능함. 왜 틀렸을까


문제 : solution함수를 정의하는건데
numbers에 리스트가 주어지면 리스트에있는 모든 수의 조합 (중복은 x) 1, 1 <<< 1 하나만 등록하는.. 세트식 ?? 그런 리스트를 다시 반환하는 함수를 만들어라. 

모든수의 조합 =  두개의 수를 뽑아서(리스트중), 두개를 더한값을 새로운 리스트에 집어넣는데, 중복되는값은 뺴고, 새로만드는 리스트는 순서를 맞춰서 정렬한다.. 