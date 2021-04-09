""""
Program Goals:
1. Get input from user (at multiple stages)
2. Convert some, but not all, inputs to INTs from STRs
3. We need to provide the user with choices:
    a. Add more values to a list
    b. Return a value at a specific index position
4. Add search algorithms to program:
    a. Random Search
    b. Linear Search
    c. Binary Search (2 Types)
"""
import random
from threading import Thread
myList = []
unique_list = []

def mainProgram():
    #continues until we say to stop while true
    while True:
     #add a way to catch bad use responses 
        try:
            print("Hello, there! Let's work with lists!")
            print("Choose from the following options. Type a number!")
            choice = input("""1. Add to a list or
2. Add a bunch of numbers to the list
3. Return a value at an index
4. Random Search
5. Linear search
6. Sort list
7. Add a bunch + sort list
8. Recursive Binary Search
9. Iterative Binary Search
10. Print list
11. Quit Program""")
            if choice == "1":
                addToList()
            elif choice == "2":
                addABunch()
            elif choice == "3":
                indexValues()
            elif choice == "4":
                randomSearch()
            elif choice == "5":
                linearSearch()
            elif choice == "6":
                sortLists(myList)
            elif choice == "7":
                compose()
            elif choice == "8":
                binSearch = input("What number are you looking for?  ")
                recursiveBinarySearch(unique_list, 0, len(unique_list)-1, int(binSearch))
            elif choice == "9":
                binSearch = input("What number are you looking for?  ")
                result = iterativeBinarySearch(unique_list, int(binSearch))
                if result != -1:
                    print("Your number is at index position {}".format(result))
                else:
                    print("Your number is not found in that list, bud!")
                    
            elif choice == "10":
                printLists()
            else:
                break
        except:
        #If the commands under try doesnt work send this. In case of errors except

            print("You caught an error!")

def addToList():
    print("Adding to a list! Great choice!")
    newItem = input("Type a integer here!   ")
    myList.append(int(newItem))

def addABunch():
    print("We're gonna add a bunch of integers to your list!")
    numToAdd = input("How many numbers do you want to add?  ")
    numRange = input("How high do you want the numbers to go?  ")
    for x in range(0, int(numToAdd)):
        myList.append(random.randint(0, int(numRange)))
    print("Your list is complete!")

def indexValues():
    print("Curious about an index position? ME TOO!")
    indexPos = input("What index position would you like to check out?")
    print(myList[int(indexPos)])

#Make linear and random search choose between unique list and myList
def randomSearch():
    print("RaNDoM sEArcH?!?")
    choose = input("Do you want to choose from your sorted list?  Y/N  ")
    if choose.lower() == "y":
        print(unique_list[random.randint(0, len(unique_list)-1)])
    else:
        print(myList[random.randint(0, len(myList)-1)])
    
def linearSearch():
    print("We're going to search each item one by one!")
    searchItem = input("What are you looking for, partner?  ")
    choose = input("Do you want to look in your sorted list?  Y/N  ")
    appCount = 0
    if choose.lower() == "y":
        for x in range(len(unique_list)):
            if unique_list[x] == int(searchItem):
                appCount = appCount + 1
                print("Your number appeared {} times in the sorted list".format(appCount))
                
#error- prints twice for unsorted, first time with sorted then unsorted
    else:
        for x in range(len(myList)):
            if myList[x] == int(searchItem):
                appCount = appCount + 1
                print("Your number appeared {} times in the unsorted list".format(appCount))


def sortLists(myList):
    for x in myList:
        if x not in unique_list:
            unique_list.append(x)
    unique_list.sort()
    showMe = input("Do you want to see your list of unique, sorted items?  Y/N  ")
    if showMe.lower() == "y":
        print(unique_list)
        
def recursiveBinarySearch(unique_list, low, high, x):
    if high >= low:
        mid = (high + low) // 2

        if unique_list[mid] == x:
            print("Your number is at index position {}".format(mid))
            return mid
        elif unique_list[mid] > x:
            return recursiveBinarySearch(unique_list, low, mid -1, x)
        else:
            return recursiveBinarySearch(unique_list, mid + 1, high, x)
    else:
        print("Your number isn't here!")

def iterativeBinarySearch(unique_list, x):
    low = 0
    high = len(unique_list)-1
    mid = 0
    while low <= high:
        mid = (high + low) // 2
        if unique_list[mid] < x:
            low = mid + 1
        elif unique_list[mid] > x:
            high = mid - 1
        else:
            return mid
    return -1

def printLists():
    if len(unique_list) == 0:
        print(myList)
    else:
        whichOne = input("Which list do you want to see? Sorted or unsorted?  ")
        if whichOne.lower() == "sorted":
            print(unique_list)
        else:
            print(myList)

#doesnt work
def compose(addABunch, sortLists):
    print("Lets do both! ")
    print(addABunch(), sortLists(), sep="")
    
    
#dunder main -> Double Underscore---dunder
if __name__== "__main__":
    mainProgram()
