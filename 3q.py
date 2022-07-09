password = str(input("Enter password to unlock the door: "))
command1 = "open"
command2 = "close"
command3= "quit"

if password != command1 and password != command2 and password != command3:
    print("Wrong password, Please try again")

#printing open if password entered correctly and print close if password 
elif password == command1:
    print("The door is now open")

elif password == command2:
    print("The door is now closed")
elif password == command3:
    print("The process terminated")