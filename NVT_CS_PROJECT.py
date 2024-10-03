
import winsound

def play_music1():
    winsound.PlaySound(None, winsound.SND_PURGE)
    #winsound.PlaySound('bgmusic.wav', winsound.SND_FILENAME+winsound.SND_LOOP+winsound.SND_ASYNC)
def chinesemusic():
    winsound.PlaySound(None, winsound.SND_PURGE)
    winsound.PlaySound('chinese.wav', winsound.SND_FILENAME+winsound.SND_LOOP+winsound.SND_ASYNC)
def indianmusic():
    winsound.PlaySound(None, winsound.SND_PURGE)
    winsound.PlaySound('indianmusic.wav', winsound.SND_FILENAME+winsound.SND_LOOP+winsound.SND_ASYNC)
def streetmusic():
    winsound.PlaySound(None, winsound.SND_PURGE)
    winsound.PlaySound('street.wav', winsound.SND_FILENAME+winsound.SND_LOOP+winsound.SND_ASYNC)
def southmusic():
    winsound.PlaySound(None, winsound.SND_PURGE)
    winsound.PlaySound('southmusic.wav', winsound.SND_FILENAME+winsound.SND_LOOP+winsound.SND_ASYNC)
def sweetmusic():
    winsound.PlaySound(None, winsound.SND_PURGE)
    winsound.PlaySound('sweetmusic.wav', winsound.SND_FILENAME+winsound.SND_LOOP+winsound.SND_ASYNC)
def breadmusic():
    winsound.PlaySound(None, winsound.SND_PURGE)
    winsound.PlaySound('breadmusic.wav', winsound.SND_FILENAME+winsound.SND_LOOP+winsound.SND_ASYNC)
    
import mysql.connector as nvt
mydb = nvt.connect(
        host="localhost",
        user="root",
        password="nikhil",
        database="management"
    )

def customerlist():
    def man():
        mydb = nvt.connect(
            host="localhost",
            user="root",
            password="nikhil",
            database="customer"
        )

        cursor = mydb.cursor()

        cursor.execute('SELECT * FROM numberofvisits')

        rows = cursor.fetchall()

        result_dict = {}

        for row in rows:
            key = row[0]
            value1 = row[1]
            value2 = row[2]
            result_dict[key] = (value1, value2)

        cursor.close()
        mydb.close()

    
        table = []
        headers = ["Name", "Phone Number", "Number of Visits"]


        name_width = 20
        phone_width = 20
        visits_width = 20


        header_row = f"| {'Name'.ljust(name_width)} | {'Phone Number'.ljust(phone_width)} | {'Number of Visits'.ljust(visits_width)} |"
        separator_row = f"+{'-' * (name_width + 2)}+{'-' * (phone_width + 2)}+{'-' * (visits_width + 2)}+"
        table.insert(2, separator_row)
        table.insert(3, header_row)
        table.insert(4, separator_row)


        for key, (value1, value2) in result_dict.items():
            row = f"| {str(key).ljust(name_width)} | {str(value1).ljust(phone_width)} | {str(value2).ljust(visits_width)} |"
            table.append(row)

        table.append(separator_row)

        formatted_table = "\n".join(table)

        return formatted_table

    print(man())

import mysql.connector


def login():
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="nikhil",
        database="management"
    )

    cursor = conn.cursor()

    employee_id = input("Enter your ID: ")
    password = input("Enter your password: ")

    select_query = """
    SELECT Designation, Name FROM Employees
    WHERE ID = %s AND Password = %s
    """
    cursor.execute(select_query, (employee_id, password))
    row = cursor.fetchone()

    if row is None:
        print("Invalid credentials. Access denied.")
        return None
    else:
        designation = row[0].lower()  # Convert designation to lowercase
        name = row[1]
        print(f"Welcome! {designation.capitalize()} {name}")  # Capitalize the first letter of the designation
        return designation, employee_id

    cursor.close()
    conn.close()



def view_details(employee_id):
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="nikhil",
        database="management"
    )

    cursor = conn.cursor()

    select_query = """
    SELECT SerialNumber, Name, Age, Designation, Salary FROM Employees
    WHERE ID = %s
    """
    cursor.execute(select_query, (employee_id,))
    row = cursor.fetchone()

    if row is None:
        print("Employee not found.")
    else:
        serial_number, name, age, designation, salary = row
        print("Employee Details:")
        print("Serial Number:", serial_number)
        print("Name:", name)
        print("Age:", age)
        print("Designation:", designation)
        print("Salary:", salary)

    cursor.close()
    conn.close()


def add_employee():
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="nikhil",
        database="management"
    )

    cursor = conn.cursor()

    serial_number = input("Enter Serial Number: ")
    name = input("Enter Name: ")
    age = input("Enter Age: ")
    designation = input("Enter Designation: ")
    employee_id = input("Enter ID: ")
    password = input("Enter Password: ")
    salary = input("Enter Salary: ")

    insert_query = """
    INSERT INTO Employees (SerialNumber, Name, Age, Designation, ID, Password, Salary)
    VALUES (%s, %s, %s, %s, %s, %s, %s)
    """
    employee_data = (serial_number, name, age, designation, employee_id, password, salary)
    cursor.execute(insert_query, employee_data)

    conn.commit()

    cursor.close()
    conn.close()


def remove_employee():
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="nikhil",
        database="management"
    )

    cursor = conn.cursor()

    serial_number = input("Enter Serial Number: ")
    delete_query = """
    DELETE FROM Employees
    WHERE SerialNumber = %s
    """
    cursor.execute(delete_query, (serial_number,))

    conn.commit()

    cursor.close()
    conn.close()


def change_employee():
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="nikhil",
        database="management"
    )

    cursor = conn.cursor()

    serial_number = input("Enter Serial Number: ")
    select_query = """
    SELECT * FROM Employees
    WHERE SerialNumber = %s
    """
    cursor.execute(select_query, (serial_number,))
    row = cursor.fetchone()

    if row is None:
        print("Employee not found.")
    else:
        print("Employee found.")
        print("Current Data:", row)

        field = input("Enter the field to be changed (Name, Age, Designation, ID, Password, Salary): ")
        new_value = input("Enter the new value: ")

        update_query = """
        UPDATE Employees
        SET {} = %s
        WHERE SerialNumber = %s
        """
        update_query = update_query.format(field)
        cursor.execute(update_query, (new_value, serial_number))

        print("Employee data updated.")

    conn.commit()

    cursor.close()
    conn.close()
   

def management():
    designation, employee_id = login()
    if designation is None:
        return

    if designation == "admin":
        print("You are an admin. You have access to modifier.")
        while True:
            print("\n---------- Options ---------------")
            print("'add' to add an employee")
            print("'remove' to remove an employee")
            print("'change' to change employee data")
            print("'viewemployees' to view all employees")
            print("'viewcustomerlist' to view all customers")
            print("'editmenu' to edit the current menu")
            print("'exit' to exit the program")
            action = input("Enter your choice: ")

            if action == "add":
                add_employee()
            elif action == "remove":
                remove_employee()
            elif action == "change":
                change_employee()
            elif action == "viewcustomerlist":
                customerlist()
            elif action=='editmenu':
                menu__edit()
            elif action == "viewemployees":
                conn = mysql.connector.connect(
                    host="localhost",
                    user="root",
                    password="nikhil",
                    database="management"
                )

                cursor = conn.cursor()

                select_query = """
                SELECT * FROM Employees
                """
                cursor.execute(select_query)

                rows = cursor.fetchall()

                print("\n--- Employees Table ---")
                print("--------------------------------------------------------------")
                print("| Serial Number | Name         | Age | Designation | Salary   |")
                print("--------------------------------------------------------------")

                for row in rows:
                    serial_number, name, age, designation, emp_id, password, salary = row
                    print(f"| {serial_number:<13} | {name:<12} | {age:<3} | {designation:<11} | {salary:<8} |")

                print("--------------------------------------------------------------")

                cursor.close()
                conn.close()

            elif action == "exit":
                print("Exiting the program...")
                welcome()
            else:
                print("Invalid option. Please try again.")

    else:
        print("You are not an admin. You have access to linited details.")
        print("\n--- Options ---")
            
        print("'viewemployees' to view all employees")
        print("'viewcustomerlist' to view all customers")
        print("'exit' to exit the program")
        view_details(employee_id)
        if action2 == "viewcustomerlist":
                customerlist()
        elif action2 == "viewemployees":
                conn = mysql.connector.connect(
                    host="localhost",
                    user="root",
                    password="nikhil",
                    database="management"
                )

                cursor = conn.cursor()

                select_query = """
                SELECT * FROM Employees
                """
                cursor.execute(select_query)

                rows = cursor.fetchall()

                print("\n--- Employees Table ---")
                print("--------------------------------------------------------------")
                print("| Serial Number | Name         | Age | Designation | Salary   |")
                print("--------------------------------------------------------------")

                for row in rows:
                    serial_number, name, age, designation, emp_id, password, salary = row
                    print(f"| {serial_number:<13} | {name:<12} | {age:<3} | {designation:<11} | {salary:<8} |")

                print("--------------------------------------------------------------")

                cursor.close()
                conn.close()

        elif action2 == "exit":
                print("Exiting the program...")
                welcome()
        else:
                print("Invalid option. Please try again.")

def menu__(T):
    menu=open(T,'r')
    f=menu.readlines()
    for i in f:
        print(i,' ')
    menu.close()




def menu_edit(T):

    menu__(T)

    opt=input('Do you want to add(A) or remove(R)')




    if opt.upper()=='A':
        menu_= open(T, "r")
        lines=menu_.readlines()
        for line in lines:
            n=line.split()[0]
        no=int(n)+1

        itm=input('enter the name(without spaces)):')

        while ' ' in itm :
            print('invalid input! dont use any spaces!\n')
            itm=input('enter the name (without spaces) ):')

        prc=input('\nenter the price of item("price"<space>"currency"):')

        while len(prc.split())!=2:
            print('invalid input! Please enter input in correct format \n')
            prc=input('enter the price of item  ( "price" <space> "currency" ) :')
        while (prc.split()[0].isdigit()==False) or (prc.split()[1].isdigit()==True) :
            print('invalid input! Please enter input in correct format\n')
            prc=input('enter the price of item  ( "price" <space> "currency" ) :')


        menu=open(T,'a')
        menu.write('  '+ str(no) +' '*(5-len(str(no))-2)+'|'+' '*5+ itm  + ' '*(22-(len(itm)+5))+'|  '+prc+'\n')

        print('done!')
        menu_.close()
        menu=open(T,'r')
        f=menu.readlines()

        for i in f:
            print(i,' ')
        menu.close()



    elif opt.upper()=='R':
        no=1
        t=0
        itm=input('\nwhich item do you want to remove(enter item code)?')
        menu= open(T, "r")
        lines = menu.readlines()
        menu= open(T, "w")
        for line in lines:
            t=t+1
            if t>5:
                if  itm not in line.split():
                    if line!='':
                        menu.write('  '+str(no)+' '*(5-len(str(no))-2)+'|'+line[6:])
                        no=no+1
            else:
                menu.write(line)
        print('done!')
        menu.close()
        menu=open(T,'r')
        f=menu.readlines()

        for i in f:
            print(i,' ')
        menu.close()

    else:
        print('invalid input!')
        menu_edit(T)




def edit_street():
    T='menu(S).txt'
    return(menu_edit(T))

def edit_south():

    T='menu(SO).txt'
    return(menu_edit(T))


def edit_chinese():

   T='menu(C).txt'
   return(menu_edit(T))


def edit_indian():

    T='menu(I).txt'

    return(menu_edit(T))

def edit_bread():

    T='menu(B).txt'

    return(menu_edit(T))


def edit_sweet():

    T='menu(SW).txt'

    return(menu_edit(T))



def menu__edit():


    while True:
        print('''
----------EDIT OPTIONS----------
1.Street Food
2.South-Indian
3.Indian
4.Chinese
5.Breads
6.deserts
7.Exit''')
        choice=input('Enter option:')

        if choice=='1':
            edit_street()
        elif choice=='2':
            edit_south()
        elif choice=='3':
            edit_indian()
        elif choice=='4':
            edit_chinese()
        elif choice=='5':
            edit_bread()
        elif choice=='6':
            edit_sweet()
        elif choice=='7':
            break
        else:
            print('invalid input!')








        

#KIKIKIKIKIKIKIKIKIKIKIKIKIKIKIKIKIKIKKIKIKIKIKIKIKIKIKIKIK#
import random

def play_game_1():
    print("ROCK PAPER SCISSORS")
    print("Enter your choice (rock, paper, or scissors):")
    player_choice = input().lower()
    choices = ["rock", "paper", "scissors"]
    computer_choice = random.choice(choices)
    if player_choice == computer_choice:
        return "It's a tie! No points awarded.", 0
    elif (player_choice == "rock" and computer_choice == "scissors") or \
         (player_choice == "paper" and computer_choice == "rock") or \
         (player_choice == "scissors" and computer_choice == "paper"):
        return "You win! Your {} beats computer's {}. You get 1 point!".format(player_choice, computer_choice), 1
    else:
        return "You lose! Computer's {} beats your {}. Computer gets 1 point!".format(computer_choice, player_choice), -1

def play_game_2():
    print("GUESS THE NUMBER")
    target_number = random.randint(1, 10)
    print("Guess a number between 1 and 10:")
    player_guess = int(input())
    if player_guess == target_number:
        return "Yay! You guessed it right! You get 1 point!", 1
    else:
        return "Oops! The correct number was {}. You lose. Computer gets 1 point!".format(target_number), -1

def play_game_3():
    print("COIN TOSS")
    print("Heads or tails? (Enter 'heads' or 'tails')")
    player_choice = input().lower()
    choices = ["heads", "tails"]
    computer_choice = random.choice(choices)
    if player_choice == computer_choice:
        return "You got it! It's {}. You get 1 point!".format(player_choice), 1
    else:
        return "Nah, it's {}. Computer gets 1 point!".format(computer_choice), -1

def play_game_4():
    print("HANGMAN")
    words = ["biryani", "naan", "samosa", "dosa", "tikka", "jalebi", "paneer", "chaat", "pulao", "ladoo", "vada", "bhelpuri", "kheer"]
    word = random.choice(words)
    guessed_letters = []
    attempts = 6
    while True:
        print("Attempts left:", attempts)
        masked_word = ""
        for letter in word:
            if letter in guessed_letters:
                masked_word += letter
            else:
                masked_word += "_"
        print("Word:", masked_word)
        if "_" not in masked_word:
            return "Woohoo! You guessed the word! You get 1 point!", 1
        elif attempts == 0:
            return "Uh-oh! You ran out of attempts. The word was {}. Computer gets 1 point!".format(word), -1
        print("Enter a letter:")
        guess = input().lower()
        if guess in guessed_letters:
            print("You already guessed that letter. Try again.")
            continue
        guessed_letters.append(guess)
        if guess not in word:
            attempts -= 1

def play_mini_games():
    player_score = 0
    computer_score = 0
    while True:
        print("\n=== WELCOME TO THE MINI GAMES ===")
        print("Select a game to play:")
        print("1. Rock, Paper, Scissors")
        print("2. Guess the Number")
        print("3. Coin Toss")
        print("4. Hangman")
        print("5. Quit")
        choice = int(input("Enter your choice (1-5): "))

        if choice == 1:
            while True:
                result, points = play_game_1()
                player_score += points
                computer_score -= points
                print("\n=== RESULT ===")
                print(result)
                print("\n=== CURRENT SCORE ===")
                print("Player: ", player_score)
                print("Computer: ", computer_score)
                play_again = input("Do you want to play again? (y/n): ")
                if play_again.lower() != "y":
                    break
        elif choice == 2:
            while True:
                result, points = play_game_2()
                player_score += points
                computer_score -= points
                print("\n=== RESULT ===")
                print(result)
                print("\n=== CURRENT SCORE ===")
                print("Player: ", player_score)
                print("Computer: ", computer_score)
                play_again = input("Do you want to play again? (y/n): ")
                if play_again.lower() != "y":
                    break
        elif choice == 3:
            while True:
                result, points = play_game_3()
                player_score += points
                computer_score -= points
                print("\n=== RESULT ===")
                print(result)
                print("\n=== CURRENT SCORE ===")
                print("Player: ", player_score)
                print("Computer: ", computer_score)
                play_again = input("Do you want to play again? (y/n): ")
                if play_again.lower() != "y":
                    break
        elif choice == 4:
            while True:
                result, points = play_game_4()
                player_score += points
                computer_score -= points
                print("\n=== RESULT ===")
                print(result)
                print("\n=== CURRENT SCORE ===")
                print("Player: ", player_score)
                print("Computer: ", computer_score)
                play_again = input("Do you want to play again? (y/n): ")
                if play_again.lower() != "y":
                    break
        elif choice == 5:
            print("\n=== FINAL SCORE ===")
            print("Player: ", player_score)
            print("Computer: ", computer_score)
            print('Your order has arrived.... Enjoy :)')
            print('Do visit us again :)')
            break
        else:
            print("Invalid choice. Please select a valid option (1-5).")
        
   



def cust():
    play_music1()
    import mysql.connector as nvt
    mydb = nvt.connect(
        host="localhost",
        user="root",
        password="nikhil",
        database="customer"
    )
    cursor=mydb.cursor()
    name = input("Enter name: ")

    valid_phno = False
    while not valid_phno:
        phno_input = input("Enter phone number: ")
        try:
            phno = int(phno_input)

            valid_phno = True
        except ValueError:
            print("Invalid phone number. Please enter a valid integer.")

    select_query = "SELECT num_visits FROM numberofvisits WHERE phno = %s"
    cursor.execute(select_query, (phno,))
    existing_row = cursor.fetchone()

    if existing_row:
        num_visits = existing_row[0] + 1
        update_query = "UPDATE numberofvisits SET num_visits = %s WHERE name = %s AND phno = %s"
        cursor.execute(update_query, (num_visits, name, phno))
    else:
        insert_query = "INSERT INTO numberofvisits (name, phno, num_visits) VALUES (%s, %s, 1)"
        cursor.execute(insert_query, (name, phno))
    mydb.commit()
    cursor.close()
    mydb.close()
    print('Welcome',name,'.We hope you enjoy your stay at NVT restaurant :)')
    




def byebye():
    print("We were glad to have you with us. Thanks for coming!")

#######  order and bill
def menu__(T):
    menu=open(T,'r')
    f=menu.readlines()
    for i in f:
        print(i,' ')
    menu.close()


def order(T,cuisine__):

    menu__(T)
    items=[]
    total=0
    itm_prc=[]
    itm_qty=[]
    order=[]
    item=input('\nwhat would you like to order?(enter item code):')

    menu_= open(T, "r")
    txt = menu_.read()
    if item.upper()=='N':
        
        return ([])
    elif item.upper() not in txt.split():
            print('\n',"please enter a valid item code!")

    else:

            menu_= open(T, "r")
            lines=menu_.readlines()
            for line in lines:
                if item == line.split()[0]:

                    itm=line.split()[2]

                    price=int(line.split()[-2])
            items.append(itm)
            itm_prc.append(price)
            qty=int(input('\nenter the quantity:'))
            itm_qty.append(qty)
            total__=price*qty
            order.append({'Category': cuisine__, 'Item': itm, 'Quantity': qty, 'Price': price,'Subtotal':total__})


    while True:
        x=input('''\n(Y)Would you like to order something else from the current sub-menu?
            or
(N)Go back to the main menu? (Y/N):''')
        if x.upper()=='Y':

            item=input('\nwhat would you like to order?(enter item code):')
            if item.upper()=='N':
                return(total)
            elif item.upper() not in txt.split():
                print("\nplease enter a valid item code!")


            else:
                menu_= open(T, "r")
                lines=menu_.readlines()
                for line in lines:
                    if item in line.split():
                        itm=line.split()[2]


                        price=int(line.split()[-2])

                        ##
                        items.append(itm)
                        itm_prc.append(price)

                        ##
                qty=int(input('\nenter the quantity:'))
                itm_qty.append(qty)
                total__=price*qty
                
                order.append({'Category': cuisine__, 'Item': itm, 'Quantity': qty, 'Price': price,'Subtotal': total__})

        else:
            if play_music1()==False:
                winsound.PlaySound(None, winsound.SND_PURGE)
                play_music1()
            return(order)





def main_menu():
    print('----------MENU----------')
    print('1. Street Food')
    print('2. Indian')
    print('3. Breads')
    print('4. South Indian')
    print('5. Chinese')
    print('6. Desserts')
    print('7. Generate Bill')
    print('8. Exit')




def generate_bill(order_details):
    print('-'*38+'BILL'+'-'*38)
    print('{:<20} | {:<20} | {:<10} | {:<10} | {:<10}'.format('Category', 'Item', 'Quantity', 'Price','Subtotal'))
    print('-' * 80)
    for order in order_details:
        print('{:<20} | {:<20} | {:<10} | {:<10} | {:<10}'.format(order['Category'], order['Item'], order['Quantity'], order['Price'],order['Subtotal']))
        print('-' * 80)
    total = sum(order['Subtotal'] for order in order_details)


    import random
    chancer=random.randint(1,3)
    if chancer%2==0:
        print ('Congrats!! You have won DISCOUNT JACKPOT')
        input('press "enter" to spin the wheel')

        dis=random.randrange(0,100)
        dis=int(dis)
        print ('Congrats!! You are getting a',dis,'%','discount')

        print('{:<69} | {:<10}'.format('Total:', total))
        total=total-(total*dis/100)
        print('{:<69} | {:<10}'.format('Total after discount :) ', total))


    else:
        print('{:<69} | {:<10}'.format('Total:', total))
    print('-'*81)
    print('''\nIt was our pleasure to host you :)
''')


def street():
    streetmusic()
    cuisine__='Street-Food'
    T='menu(S).txt'
    return(order(T,cuisine__))

def south():
    southmusic()
    cuisine__='South-Indian'

    T='menu(SO).txt'
    return(order(T,cuisine__))


def chinese():
   
   chinesemusic()
   cuisine__='Chinese'

   T='menu(C).txt'
   return(order(T,cuisine__))


def indian():
    indianmusic()
    cuisine__='Indian'

    T='menu(I).txt'

    return(order(T,cuisine__))

def bread():
    breadmusic()
    cuisine__='Bread'

    T='menu(B).txt'

    return(order(T,cuisine__))


def sweet():
    sweetmusic()
    cuisine__='Deserts'

    T='menu(SW).txt'

    return(order(T,cuisine__))



#####################################################################
def welcome():

    optioncustmang=input('Please press 1 for Customer and 2 for Management--->')
    if optioncustmang=='1':
        cust()
        order_details = []
        while True:
            main_menu()
            choice = input('Enter your choice: ')

            if choice == '1':
                order_details += street()
            elif choice == '2':
                order_details += indian()
            elif choice == '3':
                order_details += bread()
            elif choice == '5':
                order_details += chinese()
            elif choice == '4':
                order_details += south()
            elif choice == '6':
                order_details +=sweet()

            elif choice == '7':
                generate_bill(order_details)
                k=input('Would you like to play some minigames while you wait for the order?(Y/N)')
                if k.upper()=='Y':
                    play_mini_games()
                    input()
                    winsound.PlaySound(None, winsound.SND_PURGE)
                else:
                    print("Thanks for coming<3")
                    input()
                    winsound.PlaySound(None, winsound.SND_PURGE)
                
                break
            elif choice=='8':
                welcome()
            else:
                print('Invalid choice. Please try again.')



    elif optioncustmang=='2':
        management()
    else:
        byebye()
welcome()


#################################################################


