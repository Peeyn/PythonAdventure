# A simple calculator:
# Write a program that allows the user to perform basic arithmetic operations 
# (e.g., addition, subtraction, multiplication, division) on two numbers. 


#program menu
while(True):
    print("-----------------\nSimple calculator\n-----------------\nWhat do you want to do?\n1.Addition\n2.Substraction\n3.Multiplication\n4.Division\n5.Exit")
    
    try:
        x = int(input("\nChoose an option: "))

    except ValueError:
        print("\nError: An integer should be provided!\n")

    else:
        # Addition
        if(x==1):
            try:
                a = float(input("\nFirst number: "))
                b = float(input("Second number: "))
                sum = a+b

            except ValueError:
                print("\nError: A number should be provided!\n")
            
            else:
                print("\n",a,"+",b,"=",sum,"\n")

        # Substraction
        elif(x==2):
            try:
                a = float(input("\nFirst number: "))
                b = float(input("Second number: "))
                diff = a-b

            except ValueError:
                print("\nError: A number should be provided!\n")
            
            else:
                print("\n",a,"-",b,"=",diff,"\n")

        # Multiplication
        elif(x==3):
            try:
                a = float(input("\nFirst number: "))
                b = float(input("Second number: "))
                product = a*b

            except ValueError:
                print("\nError: A number should be provided!\n")
            
            else:
                print("\n",a,"*",b,"=",product,"\n")

        # Division
        elif(x==4):
            try:
                a = float(input("\nFirst number: "))
                b = float(input("Second number: "))
                quotient = a/b
            except ValueError:
                print("\nError: A number should be provided!\n")
            
            except ZeroDivisionError:
                print("\nError: Cannot divide by 0!\n")

            else:               
                print("\n",a,"/",b,"=",quotient,"\n")

        # Exit program
        elif(x==5):
            print("\nGoodbye!\n")
            break

        # Other number selected         
        else:
            print("\nError: An integer between 1 and 5 must be provided!\n")
