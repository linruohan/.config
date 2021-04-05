for method in dir(object):
    #  if callable(getattr(object,method)):
    #      print(method)
    print(method)
print('*'*10)
for method in dir(object):
    print(getattr(object,method))
