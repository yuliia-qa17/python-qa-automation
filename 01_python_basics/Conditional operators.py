age = 25
name = "Alex"
if age == 25 and name == "Alex":
    print("I'm 25 years and my name is Alex")
elif age > 25:
    print("I'm more, than 25 years")
else:
    print("I'm not 25 years")

city = "moscow"
if "M" in city == "Moscow":
    print("Moscow is a city")
else:
    print("Moscow is just a word")

#programm for ATM machine
pin = 1234
print("Enter your PIN code please")
user_pin = int(input())
if pin == user_pin:
    print("How much do you want to receive?")
else:
    print("Error. Enter the correct PIN code. You have 2 varius")
    user_pin = int(input())
    if pin == user_pin:
        print("How much do you want to receive?")
    else:
        print("Error. Enter the correct PIN code. You have 1 varius")
        user_pin = int(input())
        if pin == user_pin:
            print("How much do you want to receive?")
        else:
            print("Error. Your card is blocked. Call your bank")
