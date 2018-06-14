def sortByString(s, t):
    result = ""
    for letter in t:
        for character in s:
            if character == letter:
                result = result + letter
    return result
