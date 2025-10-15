while True:
    try:
        number1=int(input('Enter your first number: '))
        number2=int(input('Enter your second number: '))
    except ValueError:
        print("Please enter numerical values")

    while True:
    
        print("Choose an operation to perform from the menu below: ")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        operator=input('Enter your choice(1,2,3,4): ')

        while operator not in['1','2','3','4']:
            print("Enter a valid choice")
            operator=input('Enter your choice(1,2,3,4): ')

        if operator=='1':
            result=number1+number2
            print(f'The sum of {number1} and {number2} is: {result}')
        elif operator=='2':
            result=number1-number2
            print(f'The subtraction of {number1} and {number2} is: {result}')
        elif operator=='3':
            result=number1*number2
            print(f'The multiplication of {number1} and {number2} is: {result}')
        elif operator=='4':
            if number2 !=0  and number1 !=0:
                wish=input(f'Do you want to divide {number1} by {number2} (yes or no): ').lower()
                if wish == 'yes':
                    result=round(number1/number2,2)
                    print(f'The division of {number1} by {number2} is: {result}')
                elif wish=='no':
                    result=round(number2/number1,2)
                    print(f'The division of {number2} by {number1} is: {result}')      
                else:
                    print("Invalid response")
                    continue
            else:
                print("ERROR ❌.Division by zero is not allowed!!")
                continue
        action = input("\nWould you like to:\n(a) Continue with result\n(b) Start new calculation\n(c) Exit\nChoose (a/b/c): ").lower()

        if action == 'a':
            number1 = result
            try:
                number2 = int(input('Enter your next number: '))
            except ValueError:
                print("Invalid number, ending calculation.")
                break
        
        elif action == 'b':
            break
        elif action == 'c':
            print("👋 Exiting calculator. Goodbye!")
            exit()
        else:
            print("Invalid choice, ending calculation.")
            break 



    

