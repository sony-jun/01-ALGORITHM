wordList = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
numList = [3,3,3,4,4,4,5,5,5,6,6,6,7,7,7,8,8,8,8,9,9,9,10,10,10,10] # 문제에서는 1보다 큰 수를 걸려면 더 많은 시간이 필요하다고 했다
resultNum=0

word = list(input())
for i in range(len(word)):
    indexNum = wordList.index(word[i]) # 새로운 indexNum변수에 입력받은 알파벳의 위치를 기억시킨다
    resultNum += numList[indexNum] # 위치에 맞는 걸리는 초 시간을 더한다.
print(resultNum)