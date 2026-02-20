# Title: Class Average Calculator
# Author: Shai Scheinson
# Date: 02/19/2026

# Create starting empty variables
grades = []
summaryStr = ""

# Collect the total number of students in order to later queue loop
totalStudents = input("Number of students (integer): ")

# Use while-loop to ensure that the program was given valid input and allow user to retry if not
while True:
    try: # Initiate "try"-sequence to check for errors while making variable totalStudents into an integer
        totalStudents = int(totalStudents)
        if totalStudents > 0: # Check that integer is greater than 0 -- leave loop if so
            break
        else:
            totalStudents = input("Invalid input. Please enter a positive number: ")
    except ValueError: # 
        totalStudents = input("Invalid input. Please enter a number: ")

# Initiate for-loop to run code for each student
for i in range(totalStudents):
    aGrade = input("Enter student " + str(i+1) + " grade: ")
    while True:
        try: # Screen input for each students grade to ensure the input is valid
            aGrade = float(aGrade)
            if aGrade > 0:
                break
            else:
                aGrade = input("Invalid input. Please enter a positive number: ")
        except ValueError:
            aGrade = input("Invalid input. Please enter a number: ")
    # Add each inputted grade to a list of grades
    grades.append(aGrade)
    # Add each grade to a string where everything is formatted together
    summaryStr += ("student " + str(i+1) + ":\t" + str(aGrade) + "\n")


print("\nStudent #\tGrade")
average = round((sum(grades))/(len(grades)), 2) # Calculate the students average and round to the hundreths place
print(summaryStr)
print("Class Average = " + str(average) + "\n")
