def vig_encode(plaintext, key):
    plaintext = plaintext.upper()
    key = key.upper()
    ciphertext = ""
    key_index = 0
    for char in plaintext:
        if char.isalpha():
            shift = ord(key[key_index]) - ord('A')
            shifted_char = chr(((ord(char) - ord('A') + shift) % 26) + ord('A'))
            ciphertext += shifted_char
            key_index = (key_index + 1) % len(key)
        else:
            ciphertext += char
    return ciphertext

def vig_decode(ciphertext, key):
    ciphertext = ciphertext.upper()
    key = key.upper()
    plaintext = ""
    key_index = 0
    for char in ciphertext:
        if char.isalpha():
            shift = ord(key[key_index]) - ord('A')
            shifted_char = chr(((ord(char) - ord('A') - shift + 26) % 26) + ord('A'))
            plaintext += shifted_char
            key_index = (key_index + 1) % len(key)
        else:
            plaintext += char
    return plaintext
