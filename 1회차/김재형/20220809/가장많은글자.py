import sys
sys.stdin = open('가장많은글자_input.txt')


alphabet = {
    'a' : 0,    'b' : 0,    'c' : 0,
    'd' : 0,    'e' : 0,    'f' : 0,
    'g' : 0,    'h' : 0,    'i' : 0,
    'j' : 0,    'k' : 0,    'l' : 0,
    'm' : 0,    'n' : 0,    'o' : 0,
    'p' : 0,    'q' : 0,    'r' : 0,
    's' : 0,    't' : 0,    'u' : 0,
    'v' : 0,    'w' : 0,    'x' : 0,
    'y' : 0,    'z' : 0,    ' ' : 0
}


n = 0
while n != 51:
    try:
        sentence = input()
        n += 1
        for s in sentence:
            if s == ' ':
                continue
            alphabet[s] += 1
    except:
        break

for k, v in alphabet.items():
    if v == max(alphabet.values()):
        print(k,end='')
