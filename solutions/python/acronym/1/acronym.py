def abbreviate(words):
    # cleaned_words = words.replace("-", "").replace(".", "").replace("!", "").strip()
    # list_of_words = words.split(" ")
    punctuation = "!\"#$%&'()*+,./:;<=>?@[\\]^_`{|}~"
    aconymn = ""
    cleaned_word = ""
    words = words.replace("-", " ")
    for char in words:
        if char in punctuation:
            continue
        cleaned_word += char
    # return cleaned_word
    list_of_words = cleaned_word.split()
    for word in list_of_words:
        aconymn += word[0].upper()
    return aconymn
