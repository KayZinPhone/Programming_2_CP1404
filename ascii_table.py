""" value = input("Enter a character: ")

 code = ord(value)
 print("the ASCII code for {} is {}".format(value,code))

 num = int(input("Enter a number between 33 and 127: "))
 character = chr(num)
 print("The character for {} is {}".format(num, character))"""


"""MIN_VALUE = 33
MAX_VALUE =127

value = input("Enter a character: ")

code = ord(value)
print("the ASCII code for {} is {}".format(value,code))

num = int(input("Enter a number between 33 and 127: "))
character = ""
while not MIN_VALUE < num < MAX_VALUE:
    print("Please enter between {} and {}".format(MIN_VALUE, MAX_VALUE))
    num = int(input("Enter a number between 33 and 127: "))

character = chr(num)
print("The character for {} is {}".format(num, character))

"""
"""

MIN_VALUE = 33
MAX_VALUE = 127
for i in range(MIN_VALUE, MAX_VALUE+1):
    print("{}{:>2s}".format(i, chr(i)))
"""

MIN_VALUE = int(input("Enter a minimum number: "))
MAX_VALUE = int(input("Enter a maximum number: "))


def get_number(MIN_VALUE, MAX_VALUE):
    try:
        var = int(input("Enter a number between {} and {}: ".format(MIN_VALUE, MAX_VALUE)))
        while not MIN_VALUE < var < MAX_VALUE:
            print("Please enter a valid number")
            var = int(input("Enter a number between {} and {}: ".format(MIN_VALUE, MAX_VALUE)))

    except ValueError:
        print("Please enter a valid value")
        var = int(input("Enter a number between {} and {}: ".format(MIN_VALUE, MAX_VALUE)))

    print(var)



print(get_number(MIN_VALUE, MAX_VALUE))
