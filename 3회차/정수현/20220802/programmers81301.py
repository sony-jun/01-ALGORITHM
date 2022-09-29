def solution(s):
    answer = 0
    numbers = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    
    for i in range(10):
        s = s.replace(numbers[i], str(i))   # 0 부터 10 까지 각 문자열을 index와 매칭시킨 numbers라는 리스트로 replace를 실행.
    answer = int(s)
    return answer

# replace()의 blackbox를 밝혀보자.


