def flatten(iterable):
    # string_iter = ""
    want = []
    def print_all_elements(iterable):
        for item in iterable:
            if isinstance(item, list):
                print_all_elements(item)
            elif item is None:
                continue
            else:
                want.append(item)
    print_all_elements(iterable)
    return want
