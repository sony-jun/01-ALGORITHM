# https://school.programmers.co.kr/learn/courses/30/lessons/81301

word_num = { 'zero' : 0, 'one' : 1, 'two' : 2, 'three' : 3, 'four' : 4, 'five' : 5, 'six' : 6, 'seven' : 7, 'eight' : 8, 'nine' :9}

# s = "23four5six7"
def solution(s):
    answer = []
    
    for i in word_num: 
        s = s.replace(i, str(word_num[i])) # 입력된 s에 포함된 문자열을 숫자(word_num 딕셔너리의 value값)으로 바꾼다. 이때, replace는 str 키워드 인자를 필요로 하므로 str으로 변환하여야 함.
    answer = int(s) # int형으로 변환하지 않으면 return answer할 때 문자열로 출력되므로 주의!
    return answer

    # for 문을 이렇게 작성해도 된다.
    # for key, value in word_num.items(): 
    #     s = s.replace(key, str(value))

# print(solution(s)) 