"""
Name: Alysha Marin
M02_Lab.py
This program is designed to process student information and determine whether 
they qualify for the Dean's List or the Honor Roll based on their GPA. 
The user will be prompted to fill out information such as the student's
first name, last name, and GPA. This program will run 5 times or whenever the 
user wishes to stop. 
"""


def Main(): 

    studentCount = 0

    while True: 
        #stores the student's last name
        lastName = input("What is the student's last name? or enter ZZZ to quit. : ")
        #stops program if user enters 'ZZZ'
        if lastName == "ZZZ": 
            break 

        #stores the student's first name 
        firstName = input("What is the student's first name?: ")
        fullName = f'{firstName} {lastName}' #stores student's first and last name 
        
        while True: 
            try: 
                #accepts user input for gpa as a float
                gpa = float(input("What is the student's GPA?: ")) 

                #makes sure input for GPA is within the proper ranges. 
                if 0<= gpa <=4.0:
                    break 
                else: 
                    print("Please enter GPA that is between 0 and 4")
            #makes sure that GPA is a valid input.
            except ValueError:
                print("Invalid input. Enter valid GPA please.")   

        #outputs if the student has met the condition to be on the dean's list. 
        if gpa >= 3.5:
            print(fullName, "has made it on the Dean's List.")
        #outputs if the student has met the condition to be on the honor list.
        elif gpa >= 3.25: 
            print(fullName, "has made it on Honor Roll.")
        #outputs when student has not met either conditions
        else: 
            print(fullName, "has neither made it onto the Dean's List nor the Honor Roll.")
        print ()

        #allows the program to run 5 times
        studentCount += 1 
        if studentCount >= 5: 
            break 

if __name__ == "__main__":
    Main()
