print("Welcome to our soda vending machine!")

SodaDetails = {
    "Limca": 12.35,
    "Pepsi": 23.75,
    "Fanta": 16.00,
    "Coca-Cola": 41.75,
    "Sprite": 32.50,
    "Mountain Dew": 23.65
}
try:
    am = int(input("How many sodas do you want? "))
    if am == 0:
        print("Thank you for using our vending machine.")
        exit()
except ValueError:
    raise Exception("Sorry, that is not an whole number.")


print("Here are your options: Limca, Pepsi, Fanta, Coca-Cola, Sprite, Mountain Dew")
ch = str(input("Choose your soda: "))   

price = format(am * float(SodaDetails[ch]), ".2f")

if ch == "Limca" or ch == "Pepsi" or ch == "Fanta" or ch == "Coca-Cola" or ch == "Sprite" or ch == "Mountain Dew": 
    print(f"You need ${price} to buy that soda.")
    ve = str(input("Are you sure that you want to pay: "))
else:
    raise Exception("Sorry, that is not an available soda")

if ve == "True" or ve == "Yes" or ve == "yes": 
    try:
        pr = float(input("Okay, How much would you like to pay: "))
    except ValueError:
        raise Exception("Sorry, that is not a vaild payment method")
    if float(SodaDetails[ch]) > pr:
        raise Exception("Sorry, that is not enough money.")
else:
    raise Exception("Sorry, we can't give the soda for free.")

if pr > float(price):
    cho = format(pr - float(price), ".2f")
    print(f"Here is your change, ${cho}")
    print("Thank you for using our vending machine and enjoy your soda.")
elif pr == float(price):
    print("Thank you for using our vending machine and enjoy your soda.")