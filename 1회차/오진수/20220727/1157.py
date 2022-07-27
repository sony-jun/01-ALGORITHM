

#문자열 input ->대문자 변환->리스트->카운트 ->max

word = input().upper()
print(word, type(word))
capital_list = list(set(word))    #set있는 경우['M', 'P', 'I', 'S'] <class 'list'>  set 없는 경우: ['M', 'I', 'S', 'S', 'I', 'S', 'I', 'P', 'I'] <class 'list'>
print(capital_list, type(capital_list))
   #왜 set?
cnt = []

for i in capital_list:   #['I', 'M', 'S', 'P']
    count = word.count(i)
    cnt.append(count)    #[4, 1, 4, 1]

if cnt.count(max(cnt)) >= 2: #count 숫자 최대값이 중복되면  -->'builtin_function_or_method' object is not iterable
    print('?')

else:
    print(max(cnt))
    #print(capital_list[(cnt.index(max(cnt)))])



#for i in word:
 #   if number(i in cnt)
  #  print(max)
#for i in word:
 #   if word.count: 
#number = 0
#for i in word:
 #   if count(word):
  #  number += 1
    #print()