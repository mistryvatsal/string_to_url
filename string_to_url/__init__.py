# Convert the string into URL format. Explicit Encoding the string to URL format into UTF-8.


def urlifystring(string):
    res = ''
    start = False
    for char in reversed(string):
        if char != ' ':
            start = True

        if char == ' ' and start is True:
            res += '+'
        else:
            res += char
    return res[::-1]

