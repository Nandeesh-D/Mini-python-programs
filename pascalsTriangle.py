
#function to find factorial of a number
def fac(n):
    if n==0 or n==1:
        return 1
    return n*fac(n-1)

def traingle(rows):
        for i in range(rows):
            print((rows-i-1)*" ",end="")
            for j in range(i+1):
                print(int(fac(i)/(fac(i-j)*fac(j))),end=" ")
            print()
rows=int(input("Enter no.of rows: "))
traingle(rows)
