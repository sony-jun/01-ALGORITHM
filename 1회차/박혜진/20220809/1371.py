alpha = {
    'a' : 0, 'b' : 0, 'c' : 0, 'd' : 0, 'e' : 0,
    'f' : 0, 'g' : 0, 'h' : 0, 'i' : 0, 'j' : 0,
    'k' : 0, 'l' : 0, 'm' : 0, 'n' : 0, 'o' : 0,
    'p' : 0, 'q' : 0, 'r' : 0, 's' : 0, 't' : 0,
    'u' : 0, 'v' : 0, 'w' : 0, 'x' : 0, 'y' : 0, 'z' : 0
}

# import sys

# word = sys.stdin.read().replace('\n', '').replace(' ', '')
word = input()


for i in word :
    if i in alpha :
        alpha[i] += 1

max_word = []
for k, v in alpha.items() :
    if v == max(alpha.values()) :
        max_word.append(k)

print(*max_word, sep='')