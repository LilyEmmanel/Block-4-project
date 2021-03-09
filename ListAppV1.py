""""
Program Goals:
1. Get input from user (at multiple stages)
2. Convert some, but not all, inputs to INTs from STRs
3. We need to provide the user with choices:
    a. Add more values to a list
    b. Return a value at a specific index position
"""

def mainProgram():
    myList = []
    print("Hello, there! Let's work with lists!")
    print("Choose from the following options. Type a number!")
    choice = input("1. Add to a list or 2. Return a value at an index   ")
    #add a way to catch bad use responses
    if choice == "1":
        addToList()
    elif choice == "2":
        indexValues()

def addToList():
    print("Adding to a list! Great choice!")
    newItem = input("Type a integer here!   ")
    myList.append(int(newItem))

def indexValues():

#dunder main -> Double Underscore---dunder
if __name__== "__main__":
    mainProgram()
