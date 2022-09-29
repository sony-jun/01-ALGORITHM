# https://school.programmers.co.kr/learn/courses/30/lessons/81301?language=python3

# 숫자를 건넬 때 일부 자릿수를 영단어로 바꾼 카드를 건네주면 프로도는 원래 숫자를 찾는 게임입니다.

dict = {"zero" : 0,
        "one": 1,
        "two": 2,
        "three": 3,
        "four": 4,
        "five": 5,
        "six": 6,
        "seven": 7,
        "eight": 8,
        "nine": 9}
s = input()
for i in dict:
    s = s.replace(i,str(dict[i]))
print(int(s))
