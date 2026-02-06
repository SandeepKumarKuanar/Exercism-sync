def encode(plain_text):
    plain = list("abcdefghijklmnopqrstuvwxyz")
    cipher = list("zyxwvutsrqponmlkjihgfedcba")
    plain_text = plain_text.lower()
    encoded = ""
    encoded_groups = []
    for char in  plain_text:
        if char not in plain:
            if char.isdigit():
                encoded += char
            else:
                continue
        elif char == " ":
            encoded += " "
        elif char in plain:
            hand = plain.index(char)
            encoded += cipher[hand]
    
    for i in range(0, len(encoded), 5):
        encoded_groups.append(encoded[i:i+5])
    encoded = " ".join(encoded_groups)
    return encoded

def decode(ciphered_text):
    plain = list("abcdefghijklmnopqrstuvwxyz")
    cipher = list("zyxwvutsrqponmlkjihgfedcba")
    ciphered_text = ciphered_text.lower()
    decoded = ""
    for char in ciphered_text:
        if char not in cipher: 
            if char.isdigit():
                decoded += char
            else:
                continue
        elif char in cipher:
            hand = cipher.index(char)
            decoded += plain[hand]
    return decoded
