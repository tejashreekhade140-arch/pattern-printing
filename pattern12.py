n=5
# Upper part of butterfly
for i in range(1, n + 1):  # Rows increase from 1 to n

    for j in range(1, 2 * n + 1):  # Total columns are 2*n

        # Check left side and right side condition
        if j <= i or j > 2 * n - i:
            print("*", end=" ")  # Print star on both sides

        else:
            print(" ", end=" ")  # Print middle spaces

    print()  # Move cursor to next line

# Lower part of butterfly
for i in range(n, 0, -1):  # Rows decrease from n to 1

    for j in range(1, 2 * n + 1):  # Total columns are 2*n

        # Check left side and right side condition
        if j <= i or j > 2 * n - i:
            print("*", end=" ")  # Print star on both sides

        else:
            print(" ", end=" ")  # Print middle spaces

    print()  # Move cursor to next line
