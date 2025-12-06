'''ditionals are fork in road to see if they are active or not.
x = int(input("What's x?"))

y = int(input("What's y?"))

if x < y:    ##boolean expression two answers: true or false
    print("x is less than y",)   ## if conditioin is true then those things happen
elif x > y:
    print("x is more than y")   ## all questions are asked from top to bottom
else:
    print("x is equal to y")   ## this is better code long way since it's more eifficent. elif ends after condition is met.
### elif - else if any elif is met then code will end.
#### else - the default for any other for conditions
'''
x = int(input("What's x?"))

y = int(input("What's y?"))

'''if x > y or x < y:
    print("X is not equal to y")   ## try to be more eifficient with task at hand
else:
    print("x is equal to y")'''
if x != y:
    print("x is not equal to y")
else:
    print("x is equal to y")
   #  left off on 23:00