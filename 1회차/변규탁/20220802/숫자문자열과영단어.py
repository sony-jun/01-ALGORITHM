# def solution(s):
#     answer = 0

#     words = [
#         "zero", "one", "two", "three", 
#         "four", "five", "six", "seven", 
#         "eight", "nine"
#         ]
#     if type(s) == int:
#         answer = int(s)
#     else:
#         for i in range(len(words)):
#             s = s.replace(words[i], str(i))
#         answer = int(s)

#     return answer


# print(solution("one4seveneight"))




'''
<문제분석>
1478 → "one4seveneight" -> 
234567 → "23four5six7"
10203 → "1zerotwozero3"

숫자	영단어
0	zero
1	one
2	two
3	three
4	four
5	five
6	six
7	seven
8	eight
9	nine

1. replace를 써야겠다. (list / dict 선택)

'''
def solution(answer):
    
    
    num = {
    'zero' : 0,
    'one' : 1,
    'two' : 2,
    'three' : 3,
    'four' : 4,
    'five' : 5,
    'six' : 6,
    'seven' : 7,
    'eight' : 8,
    'nine' : 9
    }

    for 키 in num: # num 키값을 다 순회
        if 키 in answer: # 입력된 값안에 키값이 있는지 확인한다.
            #있으면 해당키의 벨류값으로 변경한다.
            answer = answer.replace(키, str(num[키])) # 변경된 것을 저장해라

    return answer