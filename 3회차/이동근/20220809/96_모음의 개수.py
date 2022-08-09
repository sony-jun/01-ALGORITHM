import sys

input = sys.stdin.readline

open_vowels = "aeiou"

line = input()[:-1].lower()

while line != '#':
    count = 0

    for i in line:
        if i in open_vowels:
            count += 1
    
    print(count)

    line = input()[:-1].lower()