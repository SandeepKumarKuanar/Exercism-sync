def rotate(text, key):
    if key % 26 == 0:
        return text
    small_letter = [chr(place) for place in range(97, 123)]
    cipher_small = small_letter * 2
    capital_letter = [chr(place) for place in range(65, 91)]
    cipher_captial = capital_letter * 2

    cipher = ''
    for letter in text:
        if letter in small_letter:
            place = cipher_small.index(letter)
            cipher += cipher_small[place + key]
        elif letter in capital_letter:
            place = cipher_captial.index(letter)
            cipher += cipher_captial[place + key]
        else:
            cipher += letter

    return cipher