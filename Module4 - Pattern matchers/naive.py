def check(text, pattern):
    i, j = 0, 0
    starts = []
    while i < len(text):
        if text[i] == pattern[j]:
            start = i
            while text[i] == pattern[j]:
                if j == (len(pattern) - 1):
                    starts.append(start)
                    break
                i += 1
                j += 1
        i += 1
        j = 0
    if len(starts) != 0:
        for i in starts:
            print("Pattern found on index:" + str(i))
    else:
        print("No pattern found")


check("Wyszukiwanieca wzorca", "ca")
