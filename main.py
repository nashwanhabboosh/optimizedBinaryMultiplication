def binary_multiply(x, y):
    # convert binary strings to integers
    x_int = int(x, 2)
    y_int = int(y, 2)

    # calculate the product
    product = x_int * y_int

    # convert product to binary string
    product_bin = bin(product)[2:]

    # determine the maximum length of the strings
    x_len = len(x)
    y_len = len(y)
    prod_len = len(product_bin)

    # create the table
    table = []
    table.append([' ', ' '] + list(y))
    table.append(['x', ' '] + ['-' for i in range(y_len)])
    for i, c in enumerate(x[::-1]):
        row = []
        carry = 0
        for j, d in enumerate(y[::-1]):
            val = int(c) * int(d) + carry
            carry = val // 2
            row.append(str(val % 2))
        row.append(str(carry))
        table.append([c, ' '] + row[::-1])
    table.append(['-', ' '] + ['-' for i in range(y_len+1)])
    table.append([' ', ' '] + list(product_bin.zfill(prod_len)))

    # print the table
    for i in range(len(table)):
        if i == 1 or i == 3:
            print(' '.join(table[i]))
        else:
            print(''.join(table[i]))
        if i == 2:
            print()

# example usage
binary_multiply('1011', '1101')
