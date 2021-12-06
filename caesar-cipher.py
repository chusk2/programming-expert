def caesar_cipher(string, offset):
    # ascii code for 'a' : 97 ---> 'z': 122    
    codified_ordinals = [ord(char) - offset for char in string]
    codified_chars = []
    for i in codified_ordinals:
        # ciphered char is within limits of alphabet
        if 97 <= i <= 122:
            codified_chars.append(chr(i))
        # char is off-limits. Add 26 offset to set again within limits
        else:
            codified_chars.append(chr(i+26))
    # join all characters to make a codified string
    codified_string = ''.join(codified_chars)
    return codified_string


# string = "hagshsah"
# offset = 8
# expected = "zsykzksz"

# string = "a"
# offset = 26
# expected = "a"

# string = ""
# offset = 3
# expected = ""
