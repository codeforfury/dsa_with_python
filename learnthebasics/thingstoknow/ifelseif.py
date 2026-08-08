# Problem Statement - With the help of if elseif and else print the grade.
# Author - Rajiv Das
# Date - 09-08-2026
# ----------------------------------------------------------

marks = int(input("Enter the Marks: "))
if marks >= 90:
    print("Grade A")
elif marks >= 70:
    print("Grade B")
elif marks >= 50:
    print("Grade C")
elif marks >= 35:
    print("Grade D")
else:
    print("Fail")