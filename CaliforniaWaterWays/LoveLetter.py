def caesar_cipher(text, shift):
    result = ""
    for char in text:
        if char.isupper():
            shifted_char = chr((ord(char) + shift - 65) % 26 + 65)
            result += shifted_char
        elif char.islower():
            shifted_char = chr((ord(char) + shift - 97) % 26 + 97)
            result += shifted_char
        else:
            result += char
    return result
