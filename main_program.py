from stackClass import Stack
from evalPostfix import evalPostfix
from infix2Postfix import Infix2Postfix

infix = input("중위표기식을 입력 하시오: ").split()
t_f = True
while True:
    for i in infix:
        if i not in '+-*/()' and float(i) <= 0:
            print("양수를 입력해야 합니다. 다시 입력하세요")
            infix = input("중위표기식을 입력 하시오: ").split()
            t_f = False
            break
        elif i not in '+-*/()' and float(i) > 0:
            t_f = True
    if t_f == True:
        break

postfix = Infix2Postfix(infix)
result = evalPostfix(postfix)
print('중위표기:', infix)
print('후위표기:', postfix)
print('계산결과:', result, end='\n\n')