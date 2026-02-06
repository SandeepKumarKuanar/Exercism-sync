def is_pangram(sentence):
    alphabets = [chr(i) for i in range(97, 123)]
    want = []

    for i in sentence:
        if i.lower() in alphabets:
            if i.lower() not in want:
                want.append(i)

    return bool(len(want) == len(alphabets))
