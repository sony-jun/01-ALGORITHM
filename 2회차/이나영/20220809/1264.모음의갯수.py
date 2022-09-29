while True:
    sentences = input()
    moum = ['a','e','i','o','u','A','E','I','O','U']
    result = 0
    if sentences == '#':
        break
    for i in sentences:
        if i in moum:
            result += 1
    print(result)


# 아무리봐도 틀린게없는데 계속 출력값이 5로만 나와서 30분 씨름하다가 그냥 백준에 제출해보니 맞았다고함. 
# vscode 도대체..뭐..하...

    

# sentences = input()
# moum = ['a','e','i','o','u']
# result=0

# for i in sentences():
#     if sentences == moum:
#         result =+1
            
#         print(result)