def solution(s, n):
    ls = []
    for a in s:
        if a.isspace():
            ls.append(a)
        else:
            ascii = ord(a)
            if ascii >= 65 and ascii < 91:
                if (ascii+n) >= 91:
                    ascii = (ascii+n) - 26
                    new_w = chr(ascii)
                else: 
                    new_w = chr(ascii+n)
            elif ascii >= 97 and ascii < 123:
                if (ascii+n) >= 123:
                    ascii = (ascii+n) = 26
                    new_w = chr(ascii)
                else:
                    new_w = chr(ascii+n)
            ls.append(new_w)
return ''.join(ls)
