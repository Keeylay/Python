while True:
    numstudents = int(input('How many students do you have?:'))
    for i in range(numstudents):
        if (numstudents > 0):
            numstudents = numstudents - 1
            
            for i in range(numstudents):
                # studentname = []
                # studentname.append = input("Enter Students Name: ")
                # studentgrade = []
                # studentgrade.append = input('Enter Students Grade:')
                course = ['Math', 'Science', 'Histroy']
                course = int(input('1 - Math, 2 - Science, 3 - History: '))
                print("Name: ", studentname, "Grade: ", studentgrade, "Course: ", course-1)
            if (numstudents != 0):
                continue
            else:
                

# def determinegrade(studentgrade):
#     if studentgrade >= 90 and <= 100:
#         return 'A'
#     elif studentgrade >= 80 and <= 89:
#         return 'B'
#     elif studentgrade >= 70 and <= 79:
#         return 'C'
#     elif studentgrade >= 80 and <= 69:
#         return 'D'
#     else:
#         return 'F'