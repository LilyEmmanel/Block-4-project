import random
myList = []
unique_list = []
from tkinter import *
import tkinter as tk

def mainProgram():
    while True: 
        try:
            if not unique_list:
                print("Hello, there! Let's work with lists!")
                print("Choose from the following options. Type a number!")
                choice = input("""1. Add to a list or
2. Add a bunch of numbers to the list
3. Sort list
4. Add a bunch + sort list
5. Return a value at an index
6. Recursive Binary Search
7. Iterative Binary Search
8. Print list
12. Quit Program""")
                if choice == "1":
                    addToList()
                elif choice == "2":
                    addABunch()
                elif choice == "3":
                    sortLists(myList)
                elif choice == "4":
                    compose()
                elif choice == "5":
                    indexValues()
                elif choice == "6":
                    binSearch = input("What number are you looking for?  ")
                    recursiveBinarySearch(unique_list, 0, len(unique_list)-1, int(binSearch))
                elif choice == "7":
                    binSearch = input("What number are you looking for?  ")
                    result = iterativeBinarySearch(unique_list, int(binSearch))
                    if result != -1:
                        print("Your number is at index position {}".format(result))
                    else:
                        print("Your number is not found in that list, bud!")   
                elif choice == "8":
                    printLists()
                else:
                    break
                
            if unique_list:
                print("Choose from the following options. Type a number!")
                choice = input("""1. Add to a list or 
2. Add a bunch of numbers to the list
3. Sort list
4. Add a bunch + sort list
5. Return a value at an index
6. Recursive Binary Search
7. Iterative Binary Search
8. Print list
9. Print list as tkinter
10. Random Search
11. Linear search 
12. Quit Program""")
                
                if choice == "1":
                    addToList()
                elif choice == "2":
                    addABunch()
                elif choice == "3":
                    sortLists(myList)
                elif choice == "4":
                    compose()
                elif choice == "5":
                    indexValues()
                elif choice == "6":
                    binSearch = input("What number are you looking for?  ")
                    recursiveBinarySearch(unique_list, 0, len(unique_list)-1, int(binSearch))
                elif choice == "7":
                    binSearch = input("What number are you looking for?  ")
                    result = iterativeBinarySearch(unique_list, int(binSearch))
                    if result != -1:
                        print("Your number is at index position {}".format(result))
                    else:
                        print("Your number is not found in that list, bud!")   
                elif choice == "8":
                    printLists()
                elif choice == "9":
                    tkinterList()
                elif choice == "10":
                    randomSearch()
                elif choice == "11":
                    linearSearch()
                else:
                    break
        except:
            print("You caught an error!")
    
def addToList():
    try:
        print("Adding to a list! Great choice!")
        newItem = input("Type a integer here!   ")
        myList.append(int(newItem))
    except:
        print("You caught an error!Looks like your input wasnt an integer!")
        

def addABunch():
    try:
        print("We're gonna add a bunch of integers to your list!")
        numToAdd = input("How many numbers do you want to add?  ")
        numRange = input("How high do you want the numbers to go?  ")
        for x in range(0, int(numToAdd)):
            myList.append(random.randint(0, int(numRange)))
        print("Your list is complete!")
    except:
        print("You caught an error!Check if your inputs were integers!")

def sortLists(myList):
        for x in myList:
            if x not in unique_list:
                unique_list.append(x)
        unique_list.sort()
        showMe = input("Do you want to see your list of unique, sorted items?  Y/N  ")
        if showMe.lower() == "y":
            print(unique_list)
        elif showMe.lower() == "n":
            print("Alright!Lets continue then")
        else:
            print("You caught an error!Make sure youve added to your list before this and type 'y'to see your sorted list and 'n' to continue!")
        
def compose():
    print("Lets do both! ")
    addABunch()
    sortLists(myList)
        
def indexValues():
    try:
        print("Curious about an index position? ME TOO!")
        indexPos = input("What index position would you like to check out?")
        print(myList[int(indexPos)])
    except:
        print("You caught an error!Choose a number between 0 and the total amount of numbers in your list!")

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
    try:
        if len(unique_list) == 0:
            print(myList)
        else:
            whichOne = input("Which list do you want to see? Sorted or unsorted?  ")
            if whichOne.lower() == "sorted":
                print(unique_list)
            else:
                print(myList)
    except:
        print("You caught an error!Make sure you type 'sorted' or 'unsorted'!")
        
#Future goal: Add save to file option for tkinter list
def tkinterList():
        master = tk.Tk()
        myList = tk.Listbox(master)
        myText = unique_list
        myList.insert(tk.END, myText)
        myList.pack()
        lbl = tk.Label(myList, text=myText, anchor="w", font=("Helvetica", "24"))
        lbl.pack(side="top", fill="x", anchor="w")
        master.mainloop()

def randomSearch():
    print("RaNDoM sEArcH?!?")
    choose = input("Do you want to choose from your sorted list?  Y/N  ")
    if choose.lower() == "y":
        print(unique_list[random.randint(0, len(unique_list)-1)])
    elif choose.lower() == "n":
        print(myList[random.randint(0, len(myList)-1)])
    else:
        print("You caught an error! Type 'y'for choosing from sorted list if you have one, or 'n' for choosing from the original list!")
    
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
                    
    #error- prints search for unsorted, first time with sorted then unsorted
        elif choose.lower() == "n":
            for x in range(len(myList)):
                if myList[x] == int(searchItem):
                    appCount = appCount + 1
                    print("Your number appeared {} times in the unsorted list".format(appCount))

        else:
            print("You caught an error!Make sure the item youre looking for is an integer and you answer 'y'for sorted list and 'n'for original list!")

        
if __name__== "__main__":
    mainProgram()
    


                        
