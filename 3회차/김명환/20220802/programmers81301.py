def solution(s):
    number = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    answer = s
    for i in range(len(number)):
        answer = answer.replace(number[i], str(i))
 
    return int(answer)