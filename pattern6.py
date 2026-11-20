
for i in range(1,6):
    for j in range(5-i): # This loop is used for spaces in reverse order like 4 to 0
        print(" ",end=" ")#Space print
    for k in range(i): # this loop is used for print * after space according to i 
        print("*",end=" ")#Star print 
    print()#next line 