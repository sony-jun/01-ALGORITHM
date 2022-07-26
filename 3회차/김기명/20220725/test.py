
ans = set()

def solution(numbers):
    for i in range(len(numbers)):
        for j in range(len(numbers)):
            if j != i:           # number를 순회하도록 하니까 리스트에 1,1 이런식으로 서로다른 1이 있을때 두개가 합해지지않음 !!! 
                ans.add(numbers[j] + numbers[i])      # 그래서 단순 숫자가 아닌 리스트의 구성요소를 더하게 했음
    return list(ans)

print(solution([2, 1, 3, 4, 1]))
print(solution([5,0,2,7]))