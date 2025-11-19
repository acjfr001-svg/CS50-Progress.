#Working with strings:
# Ask for name and input name fuc '=' is assign
name = input("What's your name? ").strip().title() #add that straight onto the input function, so it's changed right away.

#lstrip and rstrip strips left and right
#Split user name into 1st and last name
first, last = name.split(" ")   #assigns words to vars left to right

'''Remove whitespace from str.
name = name.strip()'''

''' This capitalizes first input
name = name.capitalize() '''

'''This also capitalizes, but every new thing;
name = name.title()'''

'''This does both, you can chain together
name = name.strip().title()'''

print(f"hello, {first}")

#{} this makes it format it.
#the 'f' makes it a f-string (format)
#print(f"Hello, {name}")  #prints Hello (name)

#Workinbg with Integers: (ints)
#In python you can use all operations in math
#interactive mode is supported by python (you can run code in terminal)

#