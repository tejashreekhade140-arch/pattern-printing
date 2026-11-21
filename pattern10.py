n=5
for i in range(1, n + 1):  # This loop control rows

    for j in range(1, n + 1):  # This loop control columns

        # Check first row, last row, first column and last column
        if i == 1 or i == n or j == 1 or j == n:
            print("*", end=" ")  # Print star on boundary

        else:
            print(" ", end=" ")  # Print space inside square

    print()  # Move cursor to next line

