Penny_Worth = 0.01
Nickel_Worth = 0.05
Dime_Worth = 0.1
Quarter_Worth = 0.25

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

def process_coins(coffee):
    change = 0
    amount = 0

    user_penny = float(input("Enter the Penny: "))
    user_nickel = float(input("Enter the Nickel: "))
    user_dimes = float(input("Enter the Dimes: "))
    user_quarter = float(input("Enter the Quarter: "))
    amount += ((user_penny * Penny_Worth) + (user_nickel * Nickel_Worth) + (user_dimes * Dime_Worth) + (user_quarter * Quarter_Worth))

    if amount < MENU[coffee]["cost"]:
        print(f"Your amount: ${amount}, is not sufficient for {coffee}")
        return 0

    elif amount > MENU[coffee]["cost"]:
        change += amount - MENU[coffee]["cost"]
        print(f"Here is your {coffee} ☕, ENJOY!")
        #round(change) # or in f-string give how much you want to round here 2 and f, also use colon, :.2f.
        print(f"Here is your change: ${change:.2f}")

    elif amount == MENU[coffee]["cost"]:
        print("The coins you provided were sufficient and equals the amount of coffee.")
        print(f"Here is your {coffee} ☕, ENJOY!")
    return change

def user_coffee(coffee):
    for i in MENU[coffee]["ingredients"]: # Here in ingredient key values are looped through so water, milk and coffee_powder is stored in i, so giving the i for resources and MENU will guarantee resource update.
        resources[i] -= MENU[coffee]["ingredients"][i]

print("MACHINE ON....!")
machine = True
while machine:

    user_request = input("What would you like? (Espresso/ Latte/ Cappuccino) ").lower()
    if user_request == "off":
        print("Going OFF....!")
        machine = False

    elif user_request == "report":
        print(resources)

    elif user_request in MENU:
        print("Please Insert Coins!")

        Amount = process_coins(user_request)

        if Amount == 0:
            continue

        user_coffee(user_request)




