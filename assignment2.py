s = input("문자열을 입력하시오 : ")

d = []
for x in s:
    d.append(ord(x)+2)
    print(d)
for i in range(0, len(d)):
    print(chr(d[i]-2))

#문자열 입력을 받는다.
#encoding / decoding
# 문자열에 ASCII 값 2씩 더해서 encoding
# encoding을 출력
# ord() 함수와 chr() 함수를 이용


#문자열 입력을 받는다.
#encoding / decoding
# 문자열에 ASCII 값 2씩 더해서 encoding
# encoding을 출력
# ord() 함수와 chr() 함수를 이용
#chr로 출력한 뒤  다시 디코딩후 출력

# 다음 과제 : 문자열을 받고 전위 표기 후위 표기로 표현하고 출력
# 스택을 이용한 과제
# 터틀을 이용해서 스택을 동적으로 보여주면 됨
