import time
print("Welcome to Trustwell Bank")
print("Please insert your card ")
time.sleep(5)

password= 1234
Trials = 3
balance=10000

while Trials != 0:      
    Pin = int(input("Please enter your 4 digit pin number: "))
    while True:
        if Pin != password:
            Trials -= 1
            print("Wrong pin Number , you have",Trials,"Trials left")
                
        else:
                print("How can we help you today?")
                print("""
                        1==balance
                        2==withdraw amount
                        3==deposit amount
                        4==exit """)
                try:
                    option=int(input("Please enter your choice: "))

                except:
                    print("please enter valid choice")

                if option == 1:
                    print(f"your current balance is {balance}")

                if option == 2:
                    withdraw_amount = int(input("please enter withdraw amount: "))
                    balance = balance - withdraw_amount
                    print(f"{withdraw_amount} is debited from your account.")
                    print(f"your updated current balance is {balance}")

                if  option == 3:
                    deposite_amount = int(input("please enter the amount to deposit: "))
                    balance = balance + deposite_amount
                    print(f"{deposite_amount} is credited to your account.")
                    print(f"your updated current balance is {balance}")

                if option == 4:
                    break
           
        

