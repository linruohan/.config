class UserDict:
    def __init__(self, dict=None):
        self.data = {}
        if dict is not None:
            self.update(dict)

    def clear(self):
        self.data.clear()

    def copy(self):
        if self.__class__ is UserDict:
            return UserDict(self.data)
        import copy
        return copy.copy(self)

    def keys(self):
        return self.data.keys()

    def items(self):
        return self.data.items()

    def values(self):
        return self.data.values()

    def __getitem__(self, key):
        return self.data[key]

    def __setitem__(self, key, value):
        self.data[key] = value

    def __repr__(self):
        return repr(self.data)

    def __cmp__(self, dict):
        if isinstance(dict, UserDict):
            return cmp(self.data, dict.data)
        else:
            return cmp(self.data, dict)

    def __len__(self):
        return len(self.data)

    def __delitem__(self, key):
        del self.data[key]
