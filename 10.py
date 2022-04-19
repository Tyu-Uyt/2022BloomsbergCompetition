def iT(num):
    if num == 1:
        return 1
    else:
        return num + iT(num - 1)

def T(num):
    return sum([iT(i) for i in range(1, num + 1)])

print(T(16))

