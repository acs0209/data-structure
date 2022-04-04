from stackClass import Stack

instr = input("문자열 입력: ")

instr_reverse = Stack()
for i in instr:
    instr_reverse.push(i)

for _ in range(instr_reverse.size()):
    print(instr_reverse.pop(), end="")