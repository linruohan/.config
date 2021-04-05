

def trim(s):
    if s==' ':
        return s
    elif s[:1]==' ':
        return trim(s[1:])
    elif s[-1:]==' ':
        return trim(s[:-1])
    else:
        print(s)


trim(' asdf ')
