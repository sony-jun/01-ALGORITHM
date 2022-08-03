import sys
sys.stdin = open('B9012.txt')

T = int(input())
for tc in range(1, T+1):
    ps = input()
    # print(ps)
    pair = []
    for i in ps:
        if i == '(':
            pair.append(i)
        elif i == ')':
            if pair: # why not 'i in pair' ? 
                # pair가 참이면 아래 명령 실행.
                # 참 = 빈목록이 아니다. 리스트에 (가 있다는 말
                pair.pop()
            else:
                print('NO')
                break
                 
    else: #for-else for문 다 돌았는데 break가 안걸렸을 때
        if len(pair) > 0:
            print('NO')
        else:
            print('YES')   

#대표적인 stack 예제 
# 왼쪽리스트 오른쪽리스트 만들어서       