import sys
sys.stdin = open("5. 행복한지 슬픈지.txt", "r")


word = input()

happy_cnt = word.count(':-)')
sad_cnt = word.count(':-(')
if happy_cnt == 0 and sad_cnt == 0:
    print('none')      
elif happy_cnt > sad_cnt:
    print('happy')
elif happy_cnt < sad_cnt:
    print('sad')
elif happy_cnt == sad_cnt:
        print('unsure')
