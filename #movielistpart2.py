#movielist
#1/12/24
#Lila and Celia 

#Init 
myList = []
movie = ""
#Functions 


def movieList():
    global movie
    print("Welcome to your movie list!")
    option = int(input("Please select the following options: \n1. Add a movie to the list \n2. View the current list \n3. Mark movie as watched \n4. Remove a task from the list \n5. Remove all tasks from the movie list \n6. Sort the list alphabetically \n7. Count the # of Items on the List\n 8. Exit the program"))
    movie = (input("Enter movie:"))
    if option==1:
        addTask()
    elif option==2:
        viewList()
    elif option ==3:
        movieWatched()
    elif option==4:
        removeMovie()
    elif option ==5:
        clearList()
    elif option ==6:
        sortList()
    elif option ==7: 
        countList()
    elif option==8:
        quit()
    cont = input("Would you like to continue?")
    if cont== "yes":
        movieList()
    if cont== "no":
        quit()
    movieList()

def addTask(): 
    myList.append(movie)
def viewList ():
    print(myList)
def movieWatched():
    myList.insert(movie, "X")
def removeMovie():
    myList.remove(movie)
def clearList():
    myList.clear()
def sortList():
    sorted(myList)
def countList():
    num = myList.__len__()
    print(num)

#main 
    
movieList()