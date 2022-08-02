def solution(s):
    answer = 0

    words = [
        "zero", "one", "two", "three", 
        "four", "five", "six", "seven", 
        "eight", "nine"
        ]
    if type(s) == int:
        answer = int(s)
    else:
        for i in range(len(words)):
            s = s.replace(words[i], str(i))
        answer = int(s)

    return answer


print(solution("one4seveneight"))
