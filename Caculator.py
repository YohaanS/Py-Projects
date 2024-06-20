try:
    op = input("Which Operation would you like: ")
   
    if op == "+": 
        try:
            n1 = float(input("Please Choose a Number or Decimal: "))
            if n1 < 0:
                raise Exception("Sorry, no numbers below zero")
            n2 = float(input("Please Choose a Number or Decimal: "))
            if n2 < 0:
                raise Exception("Sorry, no numbers below zero")
            print(n1 + n2)
        except ValueError:
            raise Exception("Sorry, that is not a number")
        exit()
    if op == "-":
        try:
            n1 = float(input("Please Choose a Number or Decimal: "))
            if n1 < 0:
                raise Exception("Sorry, no numbers below zero")
            n2 = float(input("Please Choose a Number or Decimal: "))
            if n2 < 0:
                raise Exception("Sorry, no numbers below zero")
            if n1 < n2:               
                raise Exception("Sorry, no answers below zero")
            print(n1 - n2)
        except ValueError:
            raise Exception("Sorry, that is not a number")
        exit()

    if op == "x" or op == "X" or op == "*":
        try:
            n1 = float(input("Please Choose a Number or Decimal: "))
            if n1 < 0:
                raise Exception("Sorry, no numbers below zero")
            n2 = float(input("Please Choose a Number or Decimal: "))
            if n2 < 0:
                raise Exception("Sorry, no numbers below zero")
            print(n1 * n2)
        except ValueError:
            raise Exception("Sorry, that is not a number")

    if op == "/":
        try:
            n1 = float(input("Please Choose a Number or Decimal: "))
            if n1 < 0:
                raise Exception("Sorry, no numbers below zero")
            n2 = float(input("Please Choose a Number or Decimal: "))
            if n2 < 0:
                raise Exception("Sorry, no numbers below zero")
            print(n1 / n2)
        except ValueError:
            raise Exception("Sorry, that is not a number")
        except ZeroDivisionError:
            raise Exception("Sorry, no dividing numbers by zero")
       
    
finally:
    print("\nThank you for using our calculator!\n")
