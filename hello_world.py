'''
Program:
    hello_world.py
Author:
    Jarom Diaz
Summary:
    A simple program to take and print a user message.
Last Edited:
    4/19/22
'''

def main():
    
    # A user message input is taken.
    message = str(input("What would you like to print?\n> "))
    assert(type(message) == type("")) , "Message needs to be a string."
    # The message is passed to the print function.
    print_func(message)

def print_func(message):
    '''
        print_func is a function that takes a message
    and prints it to the console.
    '''

    # The message is taken and printed
    print(message)


# The main() function is run.
if __name__ == "__main__":
    main()
