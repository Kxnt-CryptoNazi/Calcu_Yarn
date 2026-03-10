print("CHOOSE AN OPERATION")
print("1 : ADD")
print("2 : SUB")
print("3 : MULTI")
print("4 : DIVIDE")

def calcu():
    while True:
        
        choice = int(input("Enter an Operation (1/2/3/4): "))
        
        num1 = float(input("Enter Num1: "))
        num2 = float(input("Enter Num2: "))
        
        if choice == 1:
            result = num1 + num2
            print(f"{num1} + {num2} = {result}")
            
        elif choice == 2:
            result = num1 - num2
            print(f"{num1} - {num2} = {result}")
            
        elif choice == 3:
            result = num1 * num2
            print(f"{num1} x {num2} = {result}")
            
        elif choice == 4:
            if num2 != 0:
                result = num1 / num2
                print(f"{num1} / {num2} = {result}")
            else:
                print("Error! Division by zero is not allowed.")
                
        else:
            print("Invalid Choice!")

        repeat = input("Do you want to calculate again? (yes/no): ").lower()
        
        if repeat != "yes":
            print("Calculator closed.")
            break

calcu()