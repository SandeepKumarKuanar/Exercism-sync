def is_isogram(string):
    if "-" in string:
        string = string.replace("-", "")
    if " " in string:
        string = string.replace(" ", "")
    list_string = list(string.lower())
    set_string = set(list_string)

    return bool(len(list_string) == len(set_string))