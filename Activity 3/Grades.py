def menu():
    print('1. View')
    print('2. Add')
    print('3. Update')
    print('4. Delete')
    print('5. Search')
    print('6. Exit')
    print("\n")
    print("Current number of entries:")
    print(len(numbers.keys()))
    print("________________________________")
    print()

numbers = {}
ch = 0
while ch != 6:
    menu()
    ch = int(input("Pick a choice from the menu (1-5): "))
    
    if ch == 1:
        print("Grades:")
        for x in numbers.keys():
          print("Student Name: ", x, "\tGrade:", numbers[x])
          print("\n")

    elif ch == 2:
        print("Add the student name and grade: ")
        name = input("Student name: ")
        phone = input("Grade of student: ")
        numbers[name] = phone 

    elif ch == 3:
        print("Update records")
        print("Grades:")
        for x in numbers.keys():
          print("Student Name: ", x, "\tGrade:", numbers[x])
          print("\n")
        
        name = input("Student name to be updated: ")
        grade = input("Grade to be updated")

        newRecord = {name:grade}

        numbers.update(newRecord)


    elif ch == 4:
        print("Do you want to delete a single record or a whole record?")
        print("(1) for single record, (2) for whole record")
        delCh = int(input("Please enter your choice: "))
        if delCh == 1:
            print("Remove records")
            name = input("Name: ")
            if name in numbers:
                del numbers[name]
            else:
                print(name, "was not found")
        elif delCh == 2:
            numbers.clear()
            print("All records deleted!")

    elif ch == 5:
        print("Do you want to search for a student or a grade?")
        print("(1) for name search, (2) for grade search")
        selCh = int(input("Please enter your choice: "))
        if selCh == 1:
            entryName = input("Enter the name of the student you want to search: ")
            if entryName in numbers:
                print("Searched name is found in the database!")
            else:  
                print(entryName + " is not found!")
        elif selCh == 2:
            try:
                enterGrade = input("Enter the grade you want to search: ")
                key = list(numbers.keys())
                value = list(numbers.values())
                if numbers[key[value.index(enterGrade)]] == enterGrade:
                    print("The grade is found!")
                else:
                    print("Grade is not found!")
            except ValueError:
                print("Grade is not found!")


    elif ch == 6:
        print("Hello")
        
    elif ch != 6:
        menu()