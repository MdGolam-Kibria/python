def qube(num1):
    return num1 ** 3


def is_int(v):
    return type(v) is int


temp = is_int(qube(3))
print(type(qube(3)) is int)
print(temp)
