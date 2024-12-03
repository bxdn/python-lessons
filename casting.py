# To convert text into an integer, use the int function as follows:
x = '10'        # initializes x to the text "10"
y = int(x)      # converts the text "10" into the number 10, and assigns y to it
print(y + 5)    # Does not error because y is an integer, not text

# To convert numbers into text, use the str function as follows:
x = 5           # initializes x and y to the numbers 5 and 10
y = 10
x_str = str(x)  # converts x and y into strings, the text "5" and "10"
y_str = str(y)
print(y_str + x_str)    # prints ?

# To convert a decimal into an integer (ROUNDED DOWN), use the int function as well:
x = 1.54        # initializes x as the number 1.54
x = int(x)      # converts x to an integer rounded down, to 1
print(x)        # prints 1