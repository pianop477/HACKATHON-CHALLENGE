#1. gets today's date and store it in a variable 'date'

from calendar import SATURDAY
from datetime import date

date = date.today();
print(date);

#2. use today's date to get the name on the day of the week written in short form with the first letter capitalized. assign variable 'day'
import datetime
day = datetime.datetime.now()
print(day.strftime("%A"));

#3. uses if-statements to determine the today's fare following these bus fare schedule:
#monday - friday = 100
#Saturday = 60
#sunday = 80;

import datetime

date = datetime.date(2022,7,9)
now = date.weekday();

if now < 5:
    print("Bus fare is: 100");

if now == 5:
    print("Bus fare is: 60");
elif now == 6:
    print("Bus fare is: 80")

#4. sales tax challenge - task two day 1
#creating user input for square feet painted wall spaace

space_painted = float(input("Enter square feet you have painted: "));
sample_square_feet = float(115)
square_feet_per_hour = float(14.375)
gallon_used = float(1)
labour_charge_per_hour = float(20.00);

#finding the total time used to paint wall
workdone = space_painted / square_feet_per_hour

if space_painted >= 0:
    print("Your working time is: ")
    print(space_painted / square_feet_per_hour)
    print('Your Salary is: ')
    print(workdone * labour_charge_per_hour)
else:
    print("Wrong Data, please enter your space painted in square feet!")

#counting number of gallons needed for square feet painted 