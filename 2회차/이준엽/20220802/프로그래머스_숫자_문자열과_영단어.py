s= input()
dict = {
    "zero" : "0",
    "one" : "1",
    "two" : "2",
    "three" : "3",
    "four" : "4",
    "five" : "5",
    "six" : "6",
    "seven" : "7",
    "eight" : "8",
    "nine" : "9", }
for i in dict:
    if i in s:
        ### 문자열 교체를 하게되면 다시 변수를 지정해줘야한다
        ### s.replace(i,dict[i])만으로는 값을 리턴 받을수 없다.
        s = s.replace(i,dict[i])
print(int(s))