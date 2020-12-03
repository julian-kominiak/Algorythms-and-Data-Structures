with open("1.2 postfixToInfix input.txt", "r") as inputFile:
    expression = inputFile.read()

output, stack = [], []

expression = expression.split(' ')

for currentCharacter in expression:

    if currentCharacter.isnumeric():
        stack.append(currentCharacter)
    if currentCharacter in ['+', '-', '*', '/', '^']:
        output = stack[-2] + currentCharacter + stack[-1]
        stack.pop()
        stack += ""
        stack[len(stack) - 1] = str("(" + output + ")")

with open("1.2 postfixToInfix output.txt", "w") as outputFile:
    outputFile.write(str(output))
