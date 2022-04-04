from stackClass import Stack

instr = input("문자열 입력:")

palindrome = Stack()

instr = list(instr.upper())
change_instr = []

for i in instr:
    if i not in '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~' and i != ' ':
        change_instr.append(i)

for i in change_instr:
    palindrome.push(i)

value = True
for i in range(len(change_instr) // 2):
    if palindrome.pop() != change_instr[i]:
        value = False
        break

if value == True:
    print("회문입니다.")
else:
    print("회문이 아닙니다.")
