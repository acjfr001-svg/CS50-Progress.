''' #working with integers2
x = int(input("What's x?  "))
y = int(input("What's y?  ")) 
# '+' can combine strings or add ints
#int is a data type and function
# python looks at inner most parathesis first and works out 
print(x + y)

# print(int(input("What's x?")) + int(input("What's y?")) ) !! you can put it all in one line (not very [ractical.])
#left off 1:15:00 on lecture 0 '''


'''
#New data type: Float; ints with decimals.
x = float(input("What's x?  "))
y = float(input("What's y?  "))
#round function allows for rounding. round(number[, ndigits])  !!! [] = something optional
z = round(x+y)
print(f"{z:,}")   # the :, formats and adds , after every three numbers 
# floats can only represent number so accurately. '''
#ints have infinite size
# floats don't


''''
x = float(input("What's x?  "))
y = float(input("What's y?  "))
z = round(x / y, 2)
print(z)
'''
'''
x = float(input("What's x?  "))
y = float(input("What's y?  "))
z = x / y
print(f"{z:.2f}")
'''



def main():
    x = int(input("What's x?  "))
    print("x squared is", squared(x))

def squared(n):
    return n*n #This actually returns a value, not just a side effect

main()