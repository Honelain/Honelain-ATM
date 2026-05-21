pins = open('pins.txt').read().split()
for i in range(len(pins)):
    pins[i] = int(pins[i])


while True: 
    print("\n--------WELCOME TO HONELAIN ATM--------")
    print("\n OPTIONS")
    print("\n1. Withdrawal")
    print("2. Exchange")
    print("3. Change Pin")
    print("4. Exit")

    val = input("\nENTER OPTION: ")

    try:
        choice = int(val)

    except:
        print("Invalid Input")
        continue

    if choice == 1:
        print("\nOPTIONS")
        print("1.MASTER CARD")
        print("2.VISA CARD")
        print("3.Home")

        val = input("\nEnter Option: ")

        try:
            option = int(val)

        except:
            print("Invalid Input")
            continue

        if option in range(1, 3):
            print("\nOPTIONS")
            print("\n1.Withdraw from 10000 - 1000000 FCFA")
            print("2.Home")

            val = input("\nEnter option: ")
            
            try:
                option = int(val)

            except:
                print("Invalid Input")
                continue

            if option == 1:
    
                val = input("Enter Pin: ")

                try:
                    pin = int(val)

                except:
                    print("Invalid Input")
                    continue
                
                
                if pin in pins:
                    val = input("Enter Amount: ")

                    try:
                        amount = int(val)

                    except:
                        print("Invalid Input")
                        continue

                    if amount in range(10000, 1000001):
                        print("\nWithdawing ", amount, "FCFA")
                        

                    elif amount < 10000:
                        print("\nWithdrawal from 10000FCFA")
                    
                                
                    else:
                        print("\ninvalid amount")

                else: 
                    print("Invalid pin")

            elif option == 2:
                print("\nReturning...")

            else: 
                print("Invalid Input")

        elif option == 3: 
            print("\nReturning...")
            continue

        else:
            print("\nInvalid Input")
            
     
    elif choice == 2:
        print("\nOPTIONS")
        print("\n1.USD ----> 590")
        print("2.EUR ----> 615")
        print("3.GBP ----> 655")
        print("4.Home")

        val = input("\nEnter Choice: ")

        try:
            options = int(val)

        except:
            print("Invalid Input")
            continue

        if options == 1:
            print("\nINSTRUCTIONS")
            print("Minimum --->20USD")
            print("Maximum ---> 2000USD")
            
            val = input("\nEnter amount: ")

            try:
                amount = int(val)
                
            except:
                print("Invalid Input")
                continue


            if amount in range(20, 2001):
                exchange = amount * 590
                print("\n INSERT MONEY")
                print("\nExchange: ", exchange, "FCFA")

            elif amount < 20:
                print("\nBelow Minimum")

            else:
                print("\nAbove Maximum")
                


        elif options == 2:
            print("\nINSTRUCTIONS")
            print("Minimum --->20EUR")
            print("Maximum ---> 2000EUR")

            val = input("\nEnter amount: ")

            try:
                amount = int(val)

            except:
                print("Invalid Input")
                continue

            if amount in range(20, 2001):
                exchange = amount * 615
                print("\n INSERT MONEY")
                print("\nExchange: ", exchange, "FCFA")

            elif amount < 20:
                print("\nBelow Minimum")
                

            else:
                print("\nAbove Maximum")
                

        elif options == 3:
            print("\nINSTRUCTIONS")
            print("Minimum --->20GBP")
            print("Maximum ---> 2000GBP")
            
            val = input("\nEnter amount: ")

            try:
                amount = int(val)

            except:
                print("Invalid Input")
                continue

            if amount in range(20, 2001):
                exchange = amount * 655
                print("\n INSERT MONEY")
                print("\nExchange: ", exchange, "FCFA")

            elif amount < 20:
                print("\nBelow Minimum")
                continue

            else:
                print("\nAbove Maximum")
                

        elif options == 4:
            print("Returning...")

        else:
            print("\nInvalid Options")

    elif choice == 3:
        print("\n1. Continue")
        print("\n2. Home")

        val = input("Enter Option: ")

        try:
            option = int(val)

        except:
            print("Invalid Input")
            continue

        if option == 1:


            old = input("Enter Current Pin: ")

            try: 
                oldpin = int(old)

            except: 
                print("Invalid Input")
                continue
            
               
            if oldpin in pins:
                val = input("\nEnter New Pin: ")

                try:
                    newpin = int(val)

                except: 
                    print("Invalid Input")
                    continue

                if not newpin in pins:
                    i = pins.index(oldpin)
                    pins[i] = newpin
                    print("\nPin Changed") 

                    with open('pins.txt', 'w') as file:
                        for p in pins:
                            file.write(f"{p}\n")
                
                else:
                    print("Pin is already taken")
                    
            else:
                print("invalid pin")

                       
        elif option == 2:
            print("Returning...")

        else: 
            print("Invalid Input")

    elif choice == 4:
        print("\nShutting Down")
        print("GOODBYE")
        break

    else: 
        print("\nInvalid Input")


            

            




    
            

