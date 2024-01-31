"""
David Cimpoiasu, 2130140
420-LCU Computer Programming, Section 1
R. Vincent, instructor
Assignment 2
"""
import time #time function
students = [
("Anne",122,36,36,7,7,7,7), # Total 100, should be an 'A'
("Alan",130,35,30,3,2,3,2), # Total 75, should be a 'B'
("Zack",128,28,28,5,4,5,4), # Total 74, should be a 'C'
("Clara",124,32,32,5,5,5,5), # Total 84, should be a 'B'
("Bob",123,30,30,6,6,6,7), # Total 85, should be an 'A'
("Jon",129,32,32,0,0,0,0), # Total 64, should be an 'F'
]
# message is menu
message = """Welcome to the Teacher’s Simple Class Calculator. Here’s the list of options:
    A- Enter student records (Name, ID, and 6 marks separated by commas)
    B- Display the class average.
    C- Display the information for a given student
    D- List the entire class by name and ID.
    X- Exit
Select an option by entering its letter:
"""

def idf(students, i_d): # find student by id in list or find if id exists
    for a in range(0,len(students)): # Checks student one by one
        if students[a][1] == i_d:
            return students[a] # if found, returns tuple of id
    # if not found, returns id is unknowed
    d = 'Student not found or invalid id'
    return d


while True:
    command = input(message)
    if command.lower() == 'x': # Exit function
        print('Goodbye!')
        break
    if command.lower() == 'b': # Average function
        sum1 = 0 # number student
        sum2 = 0 # number grade
        for a in range(0,len(students)):
            sum1 +=1 #  adds one per student
            for b in range(2,8):
                sum2 += students[a][b] # adds the grades up
        print('The class average is', round(sum2/sum1), '\n\n\n\n\n') #prints result
        time.sleep(3)# lets the user read
    if command.lower() == 'c': #student information
        g = int(input('Enter the ID of the student: ')) # gets id from user
        f=idf(students,g) #Uses idf to get user info
        sums=0 #grade of student
        grade = '' #letter grade
        for a in range(2,8):
            sums += f[a] # sums up grade
        if sums >= 85: # finds if letter grade is A
            grade = 'A'
        elif 85 > sums >= 75:# finds if letter grade is B
            grade = 'B'
        elif 75 > sums >= 65:# finds if letter grade is C
            grade = "C"
        elif 65 > sums:# finds if letter grade is F
            grade = 'F'
        print('information for', f[0], f[1], 'Total Grade', sums, 'Letter Grade', grade) # prints result info
        print('\n\n\n')
        time.sleep(3) #lets the user read
    if command.lower() == 'd':#list class by name/id
        print('Here is the list of students:\n')
        l = []
        x=''
        for a in range(0,len(students)):
            x = students[a][0]
            r = x.capitalize()
            t = r + ' ' + str(students[a][1])
            l.append(t)
            l.sort()
        for i in range(0,len(l)):
            print(l[i])
        print('\n\n\n')
        time.sleep(3)
    
    
            
        