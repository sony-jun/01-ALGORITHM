import sys

sys.stdin = open("_2857.txt", "r")

valid = False
for i in range(5):
    FBI = input()
    if FBI.count("FBI"):
        print(i+1, end= ' ')
        valid = True

if valid == False:
    print("HE GOT AWAY!")