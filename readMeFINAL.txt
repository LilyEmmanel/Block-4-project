Software Instructions:
	The first thing to occur when running our list app program is it will print a list of options. The user must choose an option which includes adding to their
new list: such as adding one item or adding a bunch of items at once. The user can then choose to print their list,print an item at a certain index position from
their list or sort their list.The option you want to go with is sorting your list, this creates a new list called unique_list which is the items of our oiginal list 
sorted into an order of lowest to highest. It is importand to do this next because it is necessary in order to use the iterative or recursive bianary search options
(which we will talk more about later), also the random and linear search options. When you choose random and linear search options it will ask if you want 
to use them on your original list or sorted list, because of this, you will want to have both lists handy. It is important to go in this
order because many options depend on each other, for example you can't search for an item in a list you haven't made yet, or sort a list you dont have.

Binary Search:
	Binary search is much like linear search, they both search for an item in a list but take different aproaches. Linear search searches each item one by one,
while binary starts in the middle of a sorted list, and checks whether that item is greater or less than the value you're looking for, which determines whether the 
value is in the first or second half of the list. Using this approch can cut the search time in half but it also requires a sorted list. Binary search is the base 
behind two of our programs options: recursive and iterative search, that is why you need to sort your list before choosing these options. Recursive search uses the
idea of recursion, which is when one thing repeates itself, in this case when a function continues to call itself over and over until the desired value 
is found, the algorithm is often longer than the Iterative algorith.This is because the iterative search uses the idea of itertion, which means repeating a sequence
of steps until the value is found. With my program, iterative search uses a while loop to repeatedly find and compare the middle of the list or section to the value 
without continuing to call itself like recursive search. It is shorter because it is less repetetive and only loops through one set of instructions.

My Changes:
	In this program there were a few places for improvement that stood out to me the most. First I thought it was a bit confusing to print all of the options to 
the user before they had sorted their list. If I only showed the options available to them that would work without having sorted their list, they would know what order to
complete the options and not end up with any errors. I did this by using 'if' and 'if not' statements. If the user didnt have unique_list only show them the basic options and
once they sorted their list they would have access to everything.
Example below:

if not unique_list:
                print("Hello, there! Let's work with lists!")
                print("Choose from the following options. Type a number!")
                choice = input("""1. Add to a list or
2. Add a bunch of numbers to the list
3. Sort list
4. Add a bunch + sort list
5. Return a value at an index
6. Print list
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

Next, I chose to add a combined funtion. It was kind of annoying to have to go through the seporate processes of adding and sorting your list and choosing the
different options. So I added an option to add a bunch of number to the list and then inmediately sort them after, it is a quicker way to make and sort your list. I
did it by calling the two functions into a new function.
Example below:

def compose():
    print("Lets do both! ")
    addABunch()
    sortLists(myList)

Finally I decided to explore tkinter, tkinter is a addition you can import into your code. What I did was make it so the user can open up a new tkinter window 
containing their sorted list. This way you can exit out of the python file and still have your list to reference in another window if you needed it. I did this 
by creating a listbox and inserting nique_list into it.
Example below:

def tkinterList():
    master = tk.Tk()
    myList = tk.Listbox(master)
    myText = unique_list
    myList.insert(tk.END, myText)
    myList.pack()
    lbl = tk.Label(myList, text=myText, anchor="w", font=("Helvetica", "24"))
    lbl.pack(side="top", fill="x", anchor="w")
    master.mainloop()



