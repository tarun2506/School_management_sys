import mysql.connector

def FEE_MENU():
    while True:
        print("1: Fee Sturcture")
        print("2: Update Fee Structure")
        print("3: Return back to the main menu")
        print("\t\t-----------------------------------------------------------")
        choice=int(input("Enter your choice 1-3: "))
        if choice==1:
            fee_structure()
        elif choice==2:
            update_fee_structure()
        elif choice==3:
            return
        else:
            print("Wrong input, Pls select a valid option.")
            run_again = input("Press any key to continue: ")

#Defining the functions for certain tasks:

def fee_structure():
    mydb = mysql.connector.connect(host="localhost", user="root", passwd="passwor0", database="project")
    my_cursor = mydb.cursor()
    my_cursor.execute(f"select * from fee_structure")
    data = my_cursor.fetchall()
    for i in data:
        print(i)

def update_fee_structure():
    mydb = mysql.connector.connect(host="localhost", user="root", passwd="passwor0", database="project")
    my_cursor = mydb.cursor()
    Class = input("Enter the class(like-->1-3): ")
    annual_charges = int(input("Enter the new annual charges: "))
    tution_fee = int(input("Enter the new tution fee: "))
    query1 = f"update fee_structure set Annual_Charges={annual_charges} where Class='{Class}'"
    query2 = f"update fee_structure set Tution_Fee={tution_fee} where Class='{Class}'"
    my_cursor.execute(query1)
    my_cursor.execute(query2)
    mydb.commit()
    print("Fee structure has been updated successfully!")





