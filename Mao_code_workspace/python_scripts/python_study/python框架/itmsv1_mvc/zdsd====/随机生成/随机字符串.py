from random import sample
def str():
    str = ''.join(sample('AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz0123456789', 8))
    return str
s=str()
print(s)
