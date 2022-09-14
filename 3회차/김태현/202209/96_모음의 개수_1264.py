import sys
sys.stdin = open("96_모음의 개수_1264.txt", "r")

vowel = "aeiouAEIOU"

while True:

    lines = input()
    if lines == "#": break

    result = []
    for i in lines:
        if i in vowel:
            result.append(i)
            
    print(len(result))
