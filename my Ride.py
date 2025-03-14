print("Select your ride: ")
print("1. Bike")
print("2. Car")

#Take input of number 1 or 2
#Select your ride
choice = int(input("Enter your choice: "))

#user entering option 1
if ( choice == 1 ): #condition 1 ouer if statement
    print( "what type of bike? ")
    print("1. BMW")
    print("2, Harley Davidson ")

    choice2= int(input("Enter your choice2: "))
    if ( choice2 == 1 ): 
        print(" You have selected BMW")
    else:
        print("You have selected Harley Davidson")

elif( choice == 2): 
    print("What type of car")
    print("1. Mercedes Benz AMG")
    print("2. Toyota")
    choice3=int(input("enter your choice: ") )

    if choice3==1 :
        print("You have selected Mercedes Benz AMG")
    else:
        print("You have selected Toyota")
else:
    print("Wrong choice!")