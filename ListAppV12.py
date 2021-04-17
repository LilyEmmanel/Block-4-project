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
''''
Explanation:
In this function the program will begin by asking for user input naming it with the newItem variable. It then appends(adds) the int(integer) the user types to myList,
if the input isnt an integer or something goes wrong in that process the program will print the error message due to the try and except blocks.
''''
    try:
        print("Adding to a list! Great choice!")
        newItem = input("Type a integer here!   ")
        myList.append(int(newItem))
    except:
        print("You caught an error!Looks like your input wasnt an integer!")
        
def addABunch():
''''
Explanation:
We have two variables, one asking the amount of numbers(numToAdd) and the other asking the range of those numbers(numRange)they want to add.
The program uses a for loop to encorperate the numToAdd input, and uses random.randint to randomly choose that many numbers within the range of 0- the numRange input
''''
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
''''
Explanation:
We use a for loop to go through every number in myList and add it to unique_list if it isnt already there. We ask if the user wants to see the
sorted list,naming their answer showMe with a variable.Then an if, elif else to say if the response is 'y' either capital or lower case, print the list.
If 'n' continue running the program, and if its a different response print an error.
''''
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
''''
Explanation:
In this function we call two other functions,addABunch and sortLists, by doing this we tell the program to refer back to those functions for instructions
and complete them both one after the other. No need for the user to do them seperately.
''''
    print("Lets do both! ")
    addABunch()
    sortLists(myList)


def indexValues():
 ''''
Explanation:
We created a variable called indexPos and stored the results of an input function inside it. We then forced the value stored in indexPos into an
integerusing the int() function and used that variable to call a value at a cirtain index position.
''''
    try:
        print("Curious about an index position? ME TOO!")
        indexPos = input("What index position would you like to check out?")
        print(myList[int(indexPos)])
    except:
        print("You caught an error!Choose a number between 0 and the total amount of numbers in your list!")

def recursiveBinarySearch(unique_list, low, high, x):
''''
Explanation:
binSearch is an input under the option function names. And unique_list, low, high, x are variables in the fuction. We use an if, elif else statement to
say high is higher than low and mid is in between. We then start a new if,elif else saying if a number is equal to the binSearch, print that numbers index position.
If the number in the list is higher than the input go lower in the list, and if the input is higher continue going higher in the list. This works because its with
unique_list which is sorted in order from lowest to highest.
''''
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
''''
Explanation:
Here we say the lowest number is 0 and high is the highest number in the len(length) of unique_list, -1 to account for the first index position being 0 in python.
We start a while loop saying as long as high is higher than low follow the if elif else statement. If x(binsearch input)is higher than the middle number(mid)
go higher in the list,if the mid is higher than binSearch go lower in the list. The answer will end up being the mid index position -1.
''''
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
''''
Explanation:
We start with a try, except statement,it allows the program to send an error message if the instructions in this function dont work. Then an if,elif statement.
If unique_list is empty, print myList, and if not we use variables and ask the user if they want to see their sorted(unique_list) or unsorted(myList)list.
We start a new if, else statement and if the variable input is sorted print unique_list if not print my_list.
''''
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
''''
Explanation:
With tkinter it requires us to start its own loop, we call it master and it calls tk.Tk which are commands imported from the tkinter file.Then we make a variable
named 'Mylist'for the tkingter window(listbox) we're making. We then name the integers from unique_list 'myText' and insert(add) it to the tkinter listbox.
We give the font, font size and positions and end the master loop.
''''
        master = tk.Tk()
        myList = tk.Listbox(master)
        myText = unique_list
        myList.insert(tk.END, myText)
        myList.pack()
        lbl = tk.Label(myList, text=myText, anchor="w", font=("Helvetica", "24"))
        lbl.pack(side="top", fill="x", anchor="w")
        master.mainloop()

def randomSearch():
''''
Explanation:
We ask if the user wants a random number from unique_list, naming their response 'choose' with a variable. Then use if,elif else statement to say if the answer is 'y'
use random.randint to choose a random number between 0 and the len(length) of unique_list. We -1 to make up for pythons index positions starting at 0.
Then if the answer is 'n' they do the same but with myList. 
''''
    print("RaNDoM sEArcH?!?")
    choose = input("Do you want to choose from your sorted list?  Y/N  ")
    if choose.lower() == "y":
        print(unique_list[random.randint(0, len(unique_list)-1)])
    elif choose.lower() == "n":
        print(myList[random.randint(0, len(myList)-1)])
    else:
        print("You caught an error! Type 'y'for choosing from sorted list if you have one, or 'n' for choosing from the original list!")
    
def linearSearch():
''''
Explanation:
First the users is asked what theyre looking for, and if they want to search unique_list, naming that input 'searchItem' and 'choose' with variables.
If the user says 'y' check every number in the len(length) of unique_list and add 1 to the on-going count(appCount variable) that starts at 0 for every time
a number is equal to searchItem input. If the respose is 'n' do the the same but with myList.
''''
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
    


                        
