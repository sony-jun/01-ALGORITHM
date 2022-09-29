import sys
sys.stdin = open("모음의개수.txt")

while True:
    cnt = 0
    string = input()
    if string == '#':
        break
    
    for str in string:
        if str == 'a' or str == 'e' or str == 'i' or str == 'o' or str == 'u' or str == 'A' or str == 'E' or str == 'I' or str == 'O' or str =='U':
            cnt += 1
    print(cnt)