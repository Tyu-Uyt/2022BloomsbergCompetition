
seq = []

for i in range(1, 41):
    print(f'{i}/40', end='\r')
    checks = range(1, i + 1)
    current = i
    go = True
    while go:
        flag = False
        for x in reversed(checks[1:]):
            if current % x != 0:
                flag = True
                break
        if flag:
            current += i
        else:
            go = False
    seq.append(current)

while True:
    num = int(input("Enter a positive integer: ")) - 1
    print(f"Smallest divisible by 1-{num + 1}: {seq[num]}")

