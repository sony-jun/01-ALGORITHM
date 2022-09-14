import sys
sys.stdin = open("99_가장 많은 글자_1371.txt", "r")

lines = sys.stdin.read()
data = [0] * 26

for line in lines:
    if line.islower():
        data[ord(line) - 97] += 1

for i in range(26):
    if data[i] == max(data):
        print(chr(i + 97), end="")
