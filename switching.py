s = input("문자열을 입력하시오 : ")

changedString = ""
for x in s: #ord함수와 chr함수로 인코드
    changedString += chr(ord(x)+2)
print(changedString)
newString = ""
for i in range(0, len(changedString)): #다시 디코드
    newString += chr(ord(changedString[i])-2)
print(newString)
