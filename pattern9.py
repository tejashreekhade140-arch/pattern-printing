n = 9  # Taking total number of rows

# Printing upper part of diamond
for i in range(1,6):

    # Printing spaces before stars
    for j in range(5-i):
        print(" ",end=" ")

    # Printing stars in increasing order
    for k in range(2*i-1):
        print("*",end=" ")

    print()  #move to next line

# Printing lower part of diamond
for i in range(4,0,-1):

    # Printing spaces before stars
    for j in range(5-i):
        print(" ",end=" ")

    # Printing stars in decreasing order
    for k in range(2*i-1):
        print("*",end=" ")

    print()  #Move to next line