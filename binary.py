f = 13.24

while not f == 0:
    str = ""
    intNum = int(f)
    floatNum = f - intNum
    while not intNum == 0:
        
        
수정본
f = 13.6875

def toBinary(f):
while True:
    intArray = [] #정수 부분을 표현할 배열
    floatArray = [] #소수점 부분을 표현할 배열
    intNum = int(f)
    floatNum = round(f - intNum, 4)
    while not intNum == 0:
        intArray.append(int(intNum%2))
        intNum = int(intNum/2)
        if 1 == intNum :
            intArray.append(1)
            break
    firstNum = floatNum
    while True:
        floatNum *= 2
        floatNum = round(floatNum, 4)
        if 1 < floatNum:
            floatNum -= 1
            floatArray.append(1)
        elif floatNum == 1:
            floatArray.append(1)
            break
        else :
            floatArray.append(0)
        if firstNum == floatNum:
            break
    break
for i in range(len(intArray)):
    print(intArray[len(intArray)-1-i], end=" ")
print(".", end="")
for i in range(len(floatArray)):
    print(floatArray[i], end=" ")        
