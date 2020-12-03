def getPriority(operator):
    if operator == '^':
        return 3
    elif operator in ['*', '/']:
        return 2
    elif operator in ['+', '-']:
        return 1
    else:
        return 0


with open("1.2 infixToPostfix input.txt", "r") as inputFile:
    expression = inputFile.read()

output, stack = [], []

expression = expression.split(' ')

for currentCharacter in expression:

    if currentCharacter.isnumeric():
        output.append(currentCharacter)
    elif currentCharacter in ['+', '-', '*', '/', '^']:
        if not stack:
            stack.append(currentCharacter)
        elif stack and getPriority(stack[-1]) < getPriority(currentCharacter):
            stack.append(currentCharacter)
        else:
            while stack and getPriority(stack[-1]) >= getPriority(currentCharacter):
                output.append(stack[-1])
                stack.pop()
            stack.append(currentCharacter)
    elif currentCharacter == '(':
        stack.append(currentCharacter)
    elif currentCharacter == ')':
        for j in stack:
            if stack[-1] == '(':
                stack.pop()
                break
            output.append(stack[-1])
            stack.pop()
    print("Input: " + currentCharacter + " Stack: " + str(stack) + " Output: " + str(output))

while stack:
    output.append(stack[-1])
    stack.pop()

with open("1.2 infixToPostfix output.txt", "w") as outputFile:
    outputFile.write(' '.join(output))
