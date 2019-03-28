s = input("문자열을 입력하시오 : ")

d = []
a = 0
for x in s:
    d.append(ord(x)+2)
    print(d)
    a += 1
for i in range(0, len(d)):
    print(chr(d[i]-2))

#문자열 입력을 받는다.
#encoding / decoding
# 문자열에 ASCII 값 2씩 더해서 encoding
# encoding을 출력
# ord() 함수와 chr() 함수를 이용
