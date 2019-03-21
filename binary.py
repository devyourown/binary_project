#저는 이진수를 배열에 담는 방식으로 만들었습니다.
#작성자 : 

def toBinary(f):
    while True:
        intArray = [] #정수 부분을 표현할 배열
        floatArray = [] #소수점 부분을 표현할 배열
        intNum = int(f) #2로 나눌 정수 변수
        floatNum = round(f - intNum, 4) #소수점 변수
        while True: #정수를 이진수로 변환하는 반복문
            intArray.append(int(intNum%2))
            intNum = int(intNum/2)
            if 1 == intNum : #마지막에 1이 남았을 경우
                intArray.append(1)
                break
        firstNum = round(floatNum, 4) #계속 같은 값이 나오면서 반복될때를 막기위한 변수
        secondNum = round(floatNum*2, 4) if floatNum*2<1 else round(floatNum*2, 4)-1 #0.3같은 수를 방지하기 위한 변수
        secondNum = round(secondNum, 4)
        tried = 0 #secondNum을 활용하기위한 변수
        while True: #소수점 10진수를 이진수로 변환하는 반복문
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
            if firstNum == round(floatNum, 4):
                break
            if tried > 0 and secondNum == round(floatNum, 4):
                break
            tried += 1 #시도 횟수
        break
    #출력
    print(f, "->", end=" ")
    for i in range(len(intArray)):
        print(intArray[len(intArray)-1-i], end=" ") #뒤에서부터 보여줌
    print(".", end="")
    for i in range(len(floatArray)):
        print(floatArray[i], end=" ")
    print("")

f = float(input("2진수로 변환시키고 싶은 10진수를 입력하세요 : "))
toBinary(f)
