import sys
sys.stdin = open("109_행복한지_10769.txt", "r")

text = input()

isBool = False

ha = text.count(":-)")
sa = text.count(":-(")

cnt = ha - sa

if ha or sa:
    isBool = True

if isBool:
    if cnt == 0:
        print("unsure")
    if cnt > 0:
        print("happy")
    if cnt < 0:
        print("sad")
else:
    print("none")