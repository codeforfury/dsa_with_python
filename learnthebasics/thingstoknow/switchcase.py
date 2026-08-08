# Problem Statement - Given the integer day denoting the day number, print on the 
# screen which day of the week it is. Week starts from Monday and for values greater 
# than 7 or less than 1, print Invalid.

# Author - Rajiv Das
# Date - 09-08-2026
# ----------------------------------------------------------

day = int(input("Enter the number to represent the day: "))
match day:
    case 1:
        print("Monday")
    case 2:
        print("Tuesday")
    case 3:
        print("Wednesday")
    case 4:
        print("Thursday")
    case 5:
        print("Friday")
    case 6:
        print("Saturday")
    case 7:
        print("Sunday")
    case _:
        print("Invalid")