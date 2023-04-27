def binary_multiply(x, y):
    # Convert binary strings to integers
    x_int = int(x, 2)
    y_int = int(y, 2)

    # Calculate the product
    product = x_int * y_int

    # Convert the product to a binary string
    binary_product = bin(product)[2:]

    # Get the length of the binary strings
    x_len = len(x)
    y_len = len(y)
    product_len = len(binary_product)

    # Calculate the number of rows needed
    rows = max(x_len, y_len, product_len) + 2

    # Initialize the table with empty strings
    table = [['' for j in range(rows)] for i in range(4)]

    # Fill in the first row
    table[0][0] = 'x'
    for i in range(1, x_len+1):
        table[0][i] = x[i-1]
    table[0][x_len+1] = 'y'
    for i in range(1, y_len+1):
        table[0][x_len+i+1] = y[i-1]

    # Fill in the second row
    for i in range(1, max(x_len, y_len)+2):
        table[1][i] = '-'

    # Fill in the third row
    table[2][0] = 'product'
    for i in range(1, product_len+1):
        table[2][i+x_len+y_len-product_len+1] = binary_product[i-1]

    # Fill in the fourth row and print intermediate steps
    for i in range(x_len):
        if x[x_len-i-1] == '1':
            for j in range(y_len):
                if y[y_len-j-1] == '1':
                    table[3][i+j+2] = '1'
            print("  " + x + " shifted left by " + str(i) + " bit(s)")
            print("  " + "-"*len(x) + " " + y)
            print("+" + "-"*(x_len+1) + y_len*"-" + "--")
            print("  " + table[3][i+2] + " "*(x_len-i-1) + "|" + table[3][i+3:])
            print("  " + "-"*(x_len+1) + y_len*"-" + "--")
        else:
            print("  " + x + " shifted left by " + str(i) + " bit(s)")
            print("  " + "-"*len(x) + " " + y)
            print("+" + "-"*(x_len+1) + y_len*"-" + "--")
            print("  " + "0"*y_len + " "*(x_len-i-1) + "|" + "0"*(product_len-i-1))
            print("  " + "-"*(x_len+1) + y_len*"-" + "--")

    # Print the final result
    print("Final result:")
    for i in range(rows):
        for j in range(max(x_len, y_len)+2):
            print(table[j][i], end=' ')
        print()

# Example usage
binary_multiply('1011', '1101')
