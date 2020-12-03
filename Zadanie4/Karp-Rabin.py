alphabet = "ABCDE"
z = []
for i in range(0, len(alphabet)):
    z.append(i)


def h(text):
    m = len(text)
    r = len(alphabet)
    output = 0
    for i in range(1, m):
        output += z[alphabet.index(text[i - 1])] * r ** (m - i)
    output += z[alphabet.index(text[m - 1])] * r ** 0
    output %= 19
    return output


def check(text, pattern):
    size = len(pattern)
    for i in range(0, len(text) - size + 1):
        current_text = text[i: i + size]
        if h(current_text) == h(pattern):
            if current_text == pattern:
                print("Pattern found on index: " + str(i))


check("AEDBACA", "BACA")
