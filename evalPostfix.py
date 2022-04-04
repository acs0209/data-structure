from stackClass import Stack

def evalPostfix(expr):
    s = Stack()

    for i in expr:
        if i in "+-*/":
            num2 = s.pop()
            num1 = s.pop()
            if i == "+":
                s.push(num1 + num2)
            elif i == "-":
                s.push(num1 - num2)
            elif i == "*":
                s.push(num1 * num2)
            elif i == "/":
                s.push(num1 / num2)
        else:
            s.push(float(i))

    return s.pop()
