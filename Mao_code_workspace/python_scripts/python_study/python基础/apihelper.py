def info(object,spacing=10,colleapse=1):
    """
    print methods and doc strings.
    takes module,class,list,dictionary,or string.
    """
    methodList=[method for method in dir(object) if callable(getattr(object,method))]
    processFunc=colleapse and (lambda s:" ".join(s.split()))or (lambda s:s)
    print("\n".join(["%s %s"%(method.ljust(spacing),
                processFunc(str(getattr(object,method).__doc__)))for method in methodList]))

if __name__ == '__main__':
    print(info.__doc__)
