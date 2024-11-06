#Print the pyramid of numbers using for loops.
def Piramid(rows):
    for i in range(rows):
        print(" "*(rows-i-1),end="")
        for j in range(2*i+1):
            print(f"{j+1}",end=" ")
        print()


rows=int(input("Enter the number of rows for the Piramid:"))
Piramid(rows)
    
    