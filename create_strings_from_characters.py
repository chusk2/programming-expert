def create_strings_from_characters(frequencies, string1, string2):
    # populate frequency dict for string1
    unique_chars1 = set(string1)
    dic_str1 = {}
    for char in unique_chars1:
        dic_str1[char] = string1.count(char)
    # populate frequency dict for string2
    unique_chars2 = set(string2)
    dic_str2 = {}
    for char in unique_chars2:
        dic_str2[char] = string2.count(char)
    # check if there are enough characters in argument dict frequencies
    # to form the strings

    result = 2  # initially suppose there are enough for both strings
    for char, freq in dic_str1.items():
        try:
            if frequencies[char] < freq:
                result -= 1
                break
            else:
                # there were enough but now they have been used
                # so remove them from available chars dic
                frequencies[char] -= freq
        except:
            result -= 1
            print('String 1 has a char which is not in frequencies!')
            break
    
    for char, freq in dic_str2.items():
        try:
            if frequencies[char] < freq:
                result -= 1
                break
            else:
                # there were enough but now they have been used
                # so remove them from available chars dic
                frequencies[char] -= freq
        except:
            result -= 1
            print('String 1 has a char which is not in frequencies!')
            break
    
    return result

frequencies = {"h": 2, "e": 1, "l": 2, "r": 4, "a": 3, "o": 2, "d": 1, "w": 1}
string1 = "hello"
string2 = "world"
# expected result = 1
output = create_strings_from_characters(frequencies, string1, string2)
print(output)