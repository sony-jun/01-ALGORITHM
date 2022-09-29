# 리스트이용

word1 = input()
word2 = input()
word3 = input()
dicword = ['black',
    'brown',
    'red' ,
    'orange' ,
    'yellow' ,
    'green' ,
    'blue' ,
    'violet' ,
    'grey' ,
    'white' ]
idx1=dicword.index(word1)
idx2=dicword.index(word2)
idx3=dicword.index(word3)
result = ((idx1*10)+idx2)*(10**idx3)
print(result)

## 딕셔너리 이용
word1 = input()
word2 = input()
word3 = input()
dicword = {
    'black': 0,
    'brown': 1,
    'red' : 2,
    'orange' : 3,
    'yellow' : 4,
    'green' : 5,
    'blue' : 6,
    'violet' : 7,
    'grey' : 8,
    'white' : 9
}
result = ((dicword[word1]*10)+dicword[word2])*10**dicword[word3]
print(result)