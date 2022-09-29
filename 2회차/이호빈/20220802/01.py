#프로그래머스 문제 숫자 문자열과 영단어
dictionary = {"zero": 0, "one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven":7, "eight": 8, "nine": 9}
def solution(s):
    for key,value in dictionary.items():
        # key가 해당 문자열 안에 있으면
        if key in s:
            #replace는 원본을 수정할 수 없어서 다시 s에 담아줬고 key,value가 int이어서 str으로 바꿔야한다.
            s = s.replace(str(key), str(value)) 
    #정수형변환       
    return int(s) 
 
