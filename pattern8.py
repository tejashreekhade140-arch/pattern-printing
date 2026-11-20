# Printing upper part of diamond
for i in range(5,0,-1):

    # Printing spaces before stars
    for j in range(5-i):
        print(" ",end=" ")

    # Printing stars 
    for k in range(2*i-1):
        print("*",end=" ")

    print()  # Moving to next line