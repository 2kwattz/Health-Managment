#Code by 2kwattz
#Simple health managment system [Python programming for begineers]
#importing modules

import datetime

def gettime():
    return datetime.datetime.now()
    
def harrydiet():       #Calling "Harrydiet.txt" file and reading & returning its content
    f = open("harrydiet.txt", "a")
    content = f.write(value)
    print("sucessfully written\n")
    return content
    f.close()

def harryvdiet():     
    f = open("harrydiet.txt", "rt")
    content = f.read()
    print(content)
    return content
    f.close()

def harryvexc():       
    content = f.read()
    return content
    f.close()

def harryexc():
    f = open("harryexcersice.txt", "a")
    content = f.write(value4)
    print("successfully written\n")
    return content
    f.close()

def rohandiet():
    f = open("rohandiet.txt", "a")
    content = f.write(value2)
    print("Sucessfully Written\n")
    return content
    f.close()

def rohanvdiet():   
    content = f.read()
    return content
    f.close()

def hammadiet():        #
    f = open("hammadiet.txt", "a")
    content = f.write(value3)
    print("Successfully written\n")
    return content
    f.close()

def hammadvdiet():    
    f = open("hammadiet.txt", "rt")
    content = f.read()
    return content
    f.close()

def rohanexc():       
    f = open("rohanexc.txt", "a")
    content = f.write(value5)
    print("Successfully written\n")
    return content
    f.close()

def rohanvexc():     
    f = open("rohanexc.txt", "rt")
    content = f.read()
    return content
    f.close()

def hammadexc():
    f = open("hammadexc.txt", "a")
    content = f.write(value6)
    print("Successfully written\n")
    return content
    f.close()

def hammadvexc():
    f = open("hammadexc.txt")
    content = f.read()
    return content
    f.close()

#Main interface
print("Health Management System Project by 2kwattz\n")
print("Please enter the number to view client\n\n 1. Harry \t 2.Rohan \t 3.Hamad")
chooseclient = int(input())

#Harry's Package

if chooseclient == 1:
    print("\nHarry's Package\t\tDiet and Excersice")
    print("\nPress 1 to enter Diet , Press 2 to Enter excersice ")
    inerch = int(input())
    if inerch == 1:
        print("\nHarry's Diet")
        print("Press 1 to view diet\t\tPress 2 to modify diet")
        inop = int(input())
        if inop == 1:
            print(harryvdiet())
        elif inop == 2:
            print("Add to the diet . Press enter to append")
            value = input()
            harrydiet()
        else:
            print("please enter a valid number")
    elif inerch == 2:
        print("Harry's Excercise\n")
        print("Press 1 to view excercise, Press 2 to modify exercise")
        inn = int(input())
        if inn == 1:
            print("View Harry's excersise")
            print(harryvexc())
        elif inn == 2:
            print("Add to the Excercise . Press enter to append")
            value4 = input()
            harryexc()
        else:
            print("Please enter a valid number\n")
    else:
        print("Please enter a valid number")

 #Rohan's Package

elif chooseclient == 2:
    print("Rohan's Package:\t\tDiet and Excersise\n")
    print("press 1 for Diet , Press 2 for Excercise\n")
    inerch2 = int(input())
    if inerch2 == 1:
        print("Press 1 to view diet\t\tPress 2 to modify diet")
        incc = int(input())
        if incc == 1:
            print("View Rohan's Diet\n")
            print(rohanvdiet())
        elif incc == 2:
            print("Add to the diet . Press enter to append")
            value2 = input()
            rohandiet()

    elif inerch2 == 2:
        print("Rohan's Excercise . Press 1 to view , Press 2 to modify")
        incc2 = int(input())
        if incc2 == 1:
            print("View Rohan's Excercise\n")
            print(rohanvexc())
        elif incc2 ==2:
            print("Add to the Excercise . Press enter to append")
            value5 = input()
            rohanexc()

    else:
        print("Please enter a valid number")
#Hammad's Package

elif chooseclient == 3:
    print("Hammad Package\t\tDiet & Excersise\n")
    print("Press 1 to enter diet , Press 2 to enter Excersise")
    inerch3 = int(input())
    if inerch3 == 1:
        print("Hammad's Diet Package\t Press 1 to view diet , press 2 to modify diet\n")
        incc3 = int(input())
        if incc3 == 1:
            print("View Hammad's Diet")
            print(hammadvdiet())
        elif incc3 == 2:
            print("Add to the diet . Press enter to append")
            value3 = input()
            hammadiet()
        else:
            print("Please enter a valid number")

    if inerch3 == 2:
        print("Hammad's excersise\t Press 1 to view , Press 2 to modify")
        incc4 = int(input())
        if incc4 == 1:
            print("View Hammad's Excercise")
            print(hammadvexc())
        elif incc4 == 2:
            print("Add to the Excercise . Press enter to append")
            value6 = input()
            hammadexc()
        else:
            print("Please enter a valid number")
