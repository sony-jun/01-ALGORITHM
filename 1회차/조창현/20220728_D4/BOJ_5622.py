#word = 'WA'
word = input()
## 처음부터 딕셔너리로 알파벳에 해당하는 초수를 정해준다.
num_dict = {
    'ABC' : 3,
    'DEF' : 4,
    'GHI' : 5,
    'JKL' : 6,
    'MNO' : 7,
    'PQRS' : 8,
    'TUV' : 9,
    'WXZY' : 10
}
## 시간 0 으로 초기화
time = 0
## 인풋받은 단어를 알파벳 단위로 돌려
for i in word:
    #print(i)
    ## 딕셔너리도 순차적으로
    for j in num_dict:
        #print(j)
        ## 알파벳이 딕션 키값에 들어있다면
        if i in j:
            #print(j)
            ## 키 값에 맞는 초수를 누적해서 더해준다.
            time += num_dict.get(j)
print(time)