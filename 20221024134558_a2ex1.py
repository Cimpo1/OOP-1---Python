"""
David Cimpoiasu, 2130140
420-LCU Computer Programming, Section 1
R. Vincent, instructor
Assignment 2
"""
import time #time function

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

students = []#future list of students

while True:
    command = input(message)
    if command.lower() == 'x': # Exit function
        print('Goodbye!')
        time.sleep(1)
        break
    if command.lower() == 'b': # Average function
        if len(students)== 0:
            print('No students info in the program yet\n')#Make sure the program does not crash if empty
            time.sleep(2)
            continue
        sum1 = 0 # number student
        sum2 = 0 # number grade
        for a in range(0,len(students)):
            sum1 +=1 #  adds one per student
            for b in range(2,8):
                sum2 += students[a][b] # adds the grades up
        print('The class average is', round(sum2/sum1), '\n\n\n\n\n') #prints result
        time.sleep(2)# lets the user read
    if command.lower() == 'c': #student information
        if len(students) == 0:# Make sure it does not crash if list is empty
            p = 'List of students is empty'
            print(p, '\n\n')
            time.sleep(2)
            continue
        gth = input('Enter the ID of the student: ')
        if (not gth.isnumeric()) or len(gth) != 3 :#Make sure program does not crash
            print('Invalid id\n')
            time.sleep(2)
            continue
        g = int(gth) # gets id from user
        f=idf(students,g) #Uses idf to get user info
        if f == 'Student not found or invalid id':
            print(f, '\n')
            time.sleep(2)
            continue
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
        time.sleep(2) #lets the user read
    if command.lower() == 'd':#list class by name/id
        if len(students) == 0:# Make sure it does not crash if list is empty
            p = 'List of students is empty'
            print(p, '\n\n')
            time.sleep(2)
            continue
        print('Here is the list of students:\n') #Tell user list incoming
        l = []#list of name/id
        x=''#str of future name
        for a in range(0,len(students)):
            x = students[a][0]#find name
            r = x.capitalize()#capitalize name
            t = r + ' ' + str(students[a][1])#adds user id to name
            l.append(t)#adds str to list
            l.sort()#sorts list for alphabetic order multiple times(in the for loop)
        for i in range(0,len(l)):
            print(l[i])#Prints name/id one by one
        print('\n\n\n')
        time.sleep(2)#lets the user read
    if command.lower() == 'a':#Input students
        while True:
            x = input('Enter student record (separate fields by commas) or done:')#main input
            gh="Record accepted."#verifier
            if x.lower() == 'done':#exit statement
                print('List complete!\n\n\n')
                time.sleep(2)
                break
            r = x.split(',')#creating temp list
            if len(r) != 8:#verify the length
                print('Record incomplete. Record rejected.')
                gh= "Record rejected"
                continue
            #Making the statements to verify the list
            ty = r[0]
            tx= r[1]
            tz= r[2]
            ta=r[3]
            tr=r[4]
            te=r[5]
            tt=r[6]
            tu=r[7]
            if type(ty) != str or not ty.isalpha():#verifying first statement type
                print('Record invalid. Record rejected.')
                gh= 'Record rejected'
                continue
            elif len(tx) != 3 or not tx.isnumeric():#verifying second statement type and length
                print('Record invalid. Record rejected.')
                gh= 'Record rejected'
                continue
            elif len(tz) != 2 or not tz.isnumeric():#verifying third statement type and length
                print('Record invalid. Record rejected.')
                gh= 'Record rejected'
                continue
            elif len(ta) != 2 or not ta.isnumeric():#verifying fourth statement type and length
                print('Record invalid. Record rejected.')
                gh= 'Record rejected'
                continue
            elif len(tr) != 1 or not tr.isnumeric():#verifying fifth statement type and length
                print('Record invalid. Record rejected.')
                gh= 'Record rejected'
                continue
            elif len(te) != 1 or not te.isnumeric():#verifying sixth statement type and length
                print('Record invalid. Record rejected.')
                gh= 'Record rejected'
                continue
            elif len(tt) != 1 or not tt.isnumeric():#verifying seventh statement type and length
                print('Record invalid. Record rejected.')
                gh= 'Record rejected'
                continue
            elif len(tu) != 1 or not tu.isnumeric():#verifying eigth statement type and length
                print('Record invalid. Record rejected.')
                gh= 'Record rejected'
                continue
            ghh=''#verifying statement
            for a in range(0,len(students)):#verifying if name already exists
                if r[0] == students[a][0]:
                    print('Record name already exists. Record rejected.')
                    gh= 'Record rejected'
                    ghh = 'T'
                    continue
            if (idf(students,int(r[1])) != 'Student not found or invalid id') and ghh == '':#Verifying if id exists already and not reapiting itself
                print('Record id already exists. Record rejected.')
                gh= 'Record rejected'
                continue
            if gh == "Record accepted.":# Adding valid record to list
                hj =[]
                hj.append(r[0])
                for a in range(1,len(r)):
                    hj.append(int(r[a]))
                hk = tuple(hj)
                students.append(hk)
                print(gh)
                
exit()#exits if while true break