use_calc = 1
while True:
    print("1. Addition")
    print("2. Substraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")
    choice = int( input ("Enter your choice to perform the operation: "))
    
    if choice == 1:
        print("You have selected Addition operation")
        num1 = input ("Enter num1: ")
        num2 = input ("Enter num2: ")
        result = int(num1) + int(num2)
        print ("Addition: ", result)
        use_calc = int(input("Do you want to continue using the calculator(1/0): "))
        if use_calc == 1:
            continue
        else:
            break
    if choice == 2:
        print("You have selected Substraction operation")
        num1 = input ("Enter num1: ")
        num2 = input ("Enter num2: ")
        result = int(num1) - int(num2)
        print ("Substraction: ", result) 
        use_calc = int(input("Do you want to continue using the calculator(1/0): "))
        if use_calc == 1:
            continue
        else:
            break
    if choice == 3:
        print("You have selected Multiplication operation")
        num1 = input ("Enter num1: ")
        num2 = input ("Enter num2: ")
        result = int(num1) * int(num2)
        print ("Multiplication: ", result)
        use_calc = int(input("Do you want to continue using the calculator(1/0): "))
        if use_calc == 1:
            continue
        else:
            break
    if choice == 4:
        print("You have selected Division operation")
        num1 = input ("Enter num1: ")
        num2 = input ("Enter num2: ")
        result = float(num1) / float(num2)
        print ("Division: ", result)
        use_calc = int(input("Do you want to continue using the calculator(1/0): "))
        if use_calc == 1:
            continue
        else:
            break
    if choice == 5:
        break
    else:
      print ("1. Addition")
      print ("2. Substraction")
      print ("3. Multiplication")
      print ("4. Division")
      print ("5. Exit")
      print ("Rerun the program and enter the choice from the above menu.")
      exit ()
