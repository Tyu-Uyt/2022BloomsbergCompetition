seq = ['1']

for _ in range(1, 41):
    count = 1
    current_seq = ''
    read_seq = seq[-1]
    current_num = read_seq[0]
    for c in read_seq[1:]:
        if c == current_num:
            count += 1
        else:
            current_seq += f'{count}{current_num}'
            current_num = c
            count = 1
    if count != 0:
        current_seq += f'{count}{current_num}'
    seq.append(current_seq if len(current_seq) < 10 else current_seq[-10:])

while True:
    num = int(input("Enter a positive integer: "))
    print(f"Term {num} of the look-and-say sequence: {seq[num - 1]}")

