def decodeString(s):
    if s.startswith("[") and s.endswith("]"):
        s = s[1:-1]
        if s[0].isalpha() and s.find("[") == -1:
            return s
        else:
            decoded = decodeString(s[1:])
            return s[0] + decoded
    elif s[0].isdigit():
        decoded = decodeString(s[1:])
        result = ""
        for i in range(0,int(s[0])):
            result = result + decoded
        return result
    else:
        return s
