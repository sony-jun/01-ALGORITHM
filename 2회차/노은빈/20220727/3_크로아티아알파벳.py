#word = map(str,input().split()) 내가 접근한 방식
c_list = ['c=', 'c-','dz=', 'd-', 'lj', 'nj', 's=', 'z=']
#dz=을 z=보다 먼저 적어야 개수 세기 가능

#풀이 replace함수 사용 replace(현재문자,새로바꿀문자,[변경할횟수])
word = input()

for i in c_list :
    word = word.replace(i, '*')  # 크로아티아 알파벳 대신 *을 넣어 바꿔서 개수를 세줌
    #예시 : ljes=njak -> *e**ak -> 6개
print(len(word))