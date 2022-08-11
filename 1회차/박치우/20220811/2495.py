import sys
sys.stdin = open('2495.txt')

for i in range(3):
    count = 0
    lst = []
    number = list(map(str,input()))
    number.append(10)
    for j in range(len(number)-1):
        if number[j] == number[j+1]:
            count += 1
        else:
            lst.append(count+1)
            count = 0
    print(max(lst))
