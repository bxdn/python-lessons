# To get the user's input, use the input() function
name = input("Please type your name: ") # prints "Please type your name: ", pauses execution, waits for the user to type a prompt followed by a new line, and points a variable called 'name' at that prompt
print("Hello, " + name)                 # prints "Hello, <name>" where <name> is the name supplied by the user

# Input returns a string, so if you ask the user for a number, remember to convert it before treating it as a number
x = input("Please enter a number to add 5 to: ")
x = int(x)
print(x + 5)                            # prints the number the user provided + 5