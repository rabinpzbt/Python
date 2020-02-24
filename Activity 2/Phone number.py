def menu():
    print('1. Add Phone Number')
    print('2. Remove Phone Number')
    print('3. Search Phone Number')
    print('4. Print Existing Phone Numbers')
    print('5. Exit program')
    print("\n")
    print("Current number of entries:")
    print(len(numbers.keys()))
    print("________________________________")
    print()

numbers = {}
ch = 0
while ch != 5:
    menu()
    ch = int(input("Pick a choice from the menu (1-5): "))
    if ch == 1:
        print("Add a new phone number")
        entryNo = ((len(numbers.keys())) + 1)
        phone = input("Number: ")
        numbers[entryNo] = phone
        curVal = len(numbers.keys())
        print("Entry number " + str(curVal) + " with value: " + str(numbers[curVal]) + " is added to the dictionary!" + "\n")
    elif ch == 2:
        print("Telephone Numbers:")
        for x in numbers.keys():
          print("Entry No: ", x, "\tNumber:", numbers[x])
        print()
        print("Remove Phone Number. Please enter Entry Number to delete")
        entryNo = int(input("Entry Number: "))
        if entryNo in numbers:
          del numbers[entryNo]
          print("Number deleted! " + "\n")
        else:
          print(" Input entry was not found" + "\n")
    elif ch == 3:
        print("Lookup Number")
        print("If search using entry number, press 1")
        print("If search using phone number, press 2")
        choiceSearch = int(input("Search using choice number: "))
        if choiceSearch == 1:
          entryNo = int(input("Enter the entry number of the number you want to search: "))
          if entryNo in numbers:
            print("The number is", numbers[entryNo] + "\n")
          else:
            print(entryNo, "was not found" + "\n")
        else:
          try:
            enterNum = input("Enter the phone number you wish to search: ")
            key = list(numbers.keys())
            value = list(numbers.values())
            if numbers[key[value.index(enterNum)]] == enterNum:
              print("Phone Number is found!" + " #: " + numbers[key[value.index(enterNum)]])
            else:
              print("Phone Number" + numbers[key[value.index(enterNum)]] + " is not found!")
          except ValueError:
            print("Phone number is not found!")
    elif ch == 4:
        print("Telephone Numbers:")
        for x in numbers.keys():
          print("Entry No: ", x, "\tNumber:", numbers[x])
          print("\n")
    elif ch != 5:
        menu()