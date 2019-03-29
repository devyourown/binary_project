def main(): #메인함수
    infix = input("중위표기식을 입력해주세요 : ")
    postfix = infixToPostfix(infix)
    print("후위표기식: ", postfix)
    prefix = infixToPrefix(infix)
    print("전위 표기식: ", prefix)

def calOrder(operator): #연산자의 우선순위를 결정해주는 함수
    if operator is "*" or operator is "/":
        return 2
    elif operator is "+" or operator is "-":
        return 1
    else :
        print("프로그램 오류 : calOrder()")

def is_operator(op): #연산자인지 확인해주는 함수
    if op == "+" or op =="-" or op == "/" or op == "*":
        return True
    else :
        return False

def reverse(string): #뒤집어주는 함수
    reversed_string = string[::-1]

    return reversed_string

def infixToPostfix(infix): #중위표기식을 후위표기식으로 변환해주는 함수
    stack = [] #파이썬은 리스트를 스택으로 이용가능하다.
    postfix = ""
    for s in infix: #s는 받은 문자열 하나하나
        if s == '(':
            stack.append(s)
            continue
        elif s == ")": # )를 받는다면 (이 나올때까지 검색해줍니다.
            while True:
                st = stack.pop()
                if st == "(":
                    break
                else :
                    postfix += st #(이 나올때까지 후위표기식에 입력
        elif is_operator(s):
            order = calOrder(s) #순서 계산
            while len(stack) > 0 :
                top = stack[-1] # peek() 대신
                if not is_operator(top): #top이 괄호라는 의미
                    break
                if calOrder(top) > order: #스택 안에 있는 연산자가 더 높다면 스택에 있는 것 부터
                    postfix += stack.pop()
                else : # 낮다면 브레이크
                    break
            stack.append(s) #연산자를 넣어줌
        else : #숫자라면
            postfix += s #바로 후위표기식에 입력
    for s in stack: #스택에 남아있는 모든 것을 출력
        postfix += stack.pop()
    return postfix

def infixToPrefix(infix): #중위표기식을 전위표기식으로 바꾸는 함수 : 이 함수는 앞선 후위표기식으로 바꾸는 함수를 사용합니다
    reversed_infix = reverse(infix) #뒤집는 함수를 사용한다
    reversed = "" #이 변수는 괄호를 제대로 받기 위해 존재
    for i in range(0, len(infix)): #괄호는 다시 뒤집습니다.
        if reversed_infix[i] == "(":
            reversed += ")"
        elif reversed_infix[i] == ")":
            reversed += "("
        else :
            reversed += reversed_infix[i]
    prefix = infixToPostfix(reversed)  # 후위표기식 함수를 이용한다.

    prefix = reverse(prefix) #다시 뒤집습니다

    return prefix

# 이 프로그램은 중위표기식을 받아 후위와 전위로 변환해주는 프로그램입니다.

main()
