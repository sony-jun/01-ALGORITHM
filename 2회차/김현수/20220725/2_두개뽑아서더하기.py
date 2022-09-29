# https://school.programmers.co.kr/learn/courses/30/lessons/68644

def solution(numbers): # 리스트를 받음, 
    # 서로 다른 인데스에 있는 두개의 수를 뽑아 더해서 오름차순 리턴
    ans = []
    cnt_i = 0 #천번쨰 넘버 인덱스 비교값
    for i in numbers:
        cnt_i += 1
        cnt_j = 0 #두번쨰 넘버 인덱스 비교값
        for j in numbers:
            cnt_j += 1
            if cnt_i == cnt_j :
                continue #인덱스값이 같으면 넘어감 /즉 같은 수는 더하지 않는다
            else:
                ans.append(i + j)

    ans = list(set(ans)) #set함수로 중복된 숫자 제거
    answer = []
    answer = sorted(ans) #자매품으로 ans.sort()
    return answer


print(solution([2, 1, 3, 4, 1]))
print(solution([5, 0, 2, 7]))
