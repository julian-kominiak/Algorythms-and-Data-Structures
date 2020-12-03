with open("1.1 input.txt", "r") as inputFile:
    text = inputFile.read()
numbersList = text.split(';')

biggestNumber = float(numbersList[0])

for i in range(0, len(numbersList)):
    numbersList[i] = float(numbersList[i])
    if numbersList[i] > biggestNumber:
        biggestNumber = numbersList[i]

with open("1.1 output.txt", "w") as outputFile:
    outputFile.write(str(biggestNumber))
