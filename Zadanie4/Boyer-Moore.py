letters = []
values = []


def createP(pattern):
    i = 0
    while i < len(pattern):
        if letters.__contains__(pattern[i]):
            values[letters.index(pattern[i])] = i
        else:
            letters.append(pattern[i])
            values.append(i)
        i += 1


def getValueFromP(letter):
    if letters.__contains__(letter):
        return values[letters.index(letter)]
    else:
        return -1


def check(text, pattern):
    m = len(pattern)
    i = m - 1
    j = m - 1
    createP(pattern)
    while i < len(text):
        if text[i] == pattern[j]:
            while text[i] == pattern[j]:
                i -= 1
                j -= 1
            if j == -1:
                print("Pattern found on index: " + str(i))
                return
        i += m - min(j, 1 + getValueFromP(text[i]))
        j = m - 1


check("CSFBADXBCABDZABDABC", "ABDABC")
