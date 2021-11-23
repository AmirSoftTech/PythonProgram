#University result letetr grade and grade point
marks= float(input("Enter mark :")) #Enter value between 0 and 100

if marks>=80 and marks<=100:
    print("Your letter grade is A+ and grade point is 4.00")

elif marks>=75 and marks<80:
    print("Your letter grade is A and grade point is 3.75")

elif marks>=70 and marks<75:
    print("Your letter grade is A- and grade point is 3.50")

elif marks>=65 and marks<70:
    print("Your letter grade is B+ and grade point is 3.25")

elif marks >= 60 and marks <65:
    print("Your letter grade is B and grade point is 3.00")

elif marks >= 55 and marks <60:
    print("Your letter grade is B- and grade point is 2.75")

elif marks >= 50 and marks <55:
    print("Your letter grade is C+ and grade point is 2.50")

elif marks >= 45 and marks <50:
    print("Your letter grade is C and grade point is 2.25")

elif marks >= 40 and marks <45:
    print("Your letter grade is D and grade point is 2.00")

elif marks==40:
    print("Your letter grade is D and grade point is 2.00")

elif marks<40:
    print("You are failed and your letter grade is F and grade point is 0.00")
else:
    print("Invalid result!!")
