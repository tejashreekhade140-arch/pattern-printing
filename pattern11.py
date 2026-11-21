n=5
for i in range(1, n + 1):  # This loop control rows

    for j in range(1, i + 1):  # Every row increase columns

        # Check first column, last column and last row
        if j == 1 or j == i or i == n:
            print("*", end=" ")  # Print star

        else:
            print(" ", end=" ")  # Print space inside triangle

    print()  # Move cursor to next line