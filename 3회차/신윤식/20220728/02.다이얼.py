# https://www.acmicpc.net/problem/5622

# 딕셔너리에 알파벳을 키 > 문제에서 주어진 값에 1을 더하여 할당
dict_ = {
    'A' : 3,
    'B' : 3,
    'C' : 3,
    'D' : 4,
    'E' : 4,
    'F' : 4,
    'G' : 5,
    'H' : 5,
    'I' : 5,
    'J' : 6,
    'K' : 6,
    'L' : 6,
    'M' : 7,
    'N' : 7,
    'O' : 7,
    'P' : 8,
    'Q' : 8,
    'R' : 8,
    'S' : 8,
    'T' : 9,
    'U' : 9,
    'V' : 9,
    'W' : 10,
    'X' : 10,
    'Y' : 10,
    'Z' : 10,
}

time = 0
input_word = input()

for word in input_word:
    time += dict_[word]

print(time)