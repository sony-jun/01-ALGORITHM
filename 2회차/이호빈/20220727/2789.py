alphabet = ['C','A','M','B','R','I','D','G','E']
A = input()

email = ''.join(x for x in A if x not in alphabet) #string join을 활용해서 포함되지 않은 값들을 새로운 문자열 반환

print(email)