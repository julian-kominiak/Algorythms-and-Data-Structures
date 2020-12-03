def caesarCipher(message, shift):
    cipheredMessage = ""
    for letter in message:
        value = (ord(letter) + shift) % 127
        if value < 32:
            value += 95
        cipheredMessage += chr(value)
    print(cipheredMessage)


caesarCipher("aBc", 21)
caesarCipher("vWx", -21)
