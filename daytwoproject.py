#personality test program 

#creating variables for user input for book purchased

book_purchased = int(input("Enter number of Books You have purchaed: "))
if book_purchased == 0:
    print('Your Bonus Point is: 0')

elif book_purchased == 1:
    print("Your Bonus Point is: 6")


elif book_purchased == 2:
    print("Your Bonus Point is: 16")

elif book_purchased == 3:
    print("Your Bonus Point is: 32")
elif book_purchased >= 4:
    print("Your Bonus Point is: 60")

#challenge 2: task two
#write python program that takes user inputs and determines what career the user should learn

#creating list of careers
favorite_career = str(input(""))
careers = ["Teacher", "Doctor", "Programmer", "Researcher", "Surveyor"]
print(careers)

career_advice = ["read more books", "observe personal hygiene", "spend your time in coding", "read more journals", "read more maps"]

career_questions = ["is it your favorite choice?", "can you work at any area?", "are you competent to this work?", ]

