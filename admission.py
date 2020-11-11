import mysql.connector

def ADM_MENU():
    while True:
        print("1: Admission Details")
        print("2: Show Admission Details")
        print("3: Search Admission Details")
        print("4: Deletion Of Details")
        print("5: Update Admission Details")
        print("6: Return back to main menu")
        print("\t\t-----------------------------------------------------------")
        choice = int(input("Enter your choice 1-6: "))
        if choice==1:
            admin_details()
        elif choice==2:
            show_admission_details()
        elif choice==3:
            search()
        elif choice==4:
            deletion_of_details()
        elif choice==5:
            update_admission_details()
        elif choice==6:
            return
        else:
            print("Wrong input, Pls select a valid option.")
            run_again = input("Press any key to continue")

#Defining the functions for certain tasks:

def admin_details():
    try:
        mydb = mysql.connector.connect(host="localhost", user="root", passwd="passwor0", database="project")
        my_cursor = mydb.cursor()
        admission_num = int(input("Enter the admission number: "))
        student_name = input("Enter student name: ")
        address = input("Enter the address: ")
        phone_num = int(input("Enter the phone number: "))
        student_class = int(input("Enter the class: "))

        query = f"insert into admission(admission_num,student_name,address,phone_num,student_class)values({admission_num},'{student_name}','{address}',{phone_num},{student_class})"
        my_cursor.execute(query)
        mydb.commit()
        mydb.close()
        my_cursor.close()
        print("Details have been pushed to the admission table successfully!")
    except:
        print("Error")


def show_admission_details():
    mydb = mysql.connector.connect(host="localhost", user="root", passwd="passwor0", database="project")
    my_cursor = mydb.cursor()
    my_cursor.execute("Select * from admission")
    data = my_cursor.fetchall()
    for fields in data:
        print(fields)
    

def search():
    mydb = mysql.connector.connect(host="localhost", user="root", passwd="passwor0", database="project")
    my_cursor = mydb.cursor()
    adm_num = int(input("Enter student's admission number: "))
    my_cursor.execute(f"Select * from admission where admission_num={adm_num}")
    data = my_cursor.fetchall()
    print(data)

def deletion_of_details():
    mydb = mysql.connector.connect(host="localhost", user="root", passwd="passwor0", database="project")
    my_cursor = mydb.cursor()
    adm_num = int(input("Enter student's admission number: "))
    my_cursor.execute(f"delete from admission where admission_num={adm_num}")
    mydb.commit()
    print("Data deleted successfully!")

def update_admission_details():
    # mydb = mysql.connector.connect(host="localhost", user="root", passwd="passwor0", database="project")
    # my_cursor = mydb.cursor()
    #Options for updation:
    print("1: Update name")
    print("2: Update address")
    print("3: Update phone number")
    print("4: Return back to the main menu")
    choice=int(input("Enter your choice 1-4: "))
    if choice==1:
        update_name()
    elif choice==2:
        update_address()
    elif choice==3:
        update_phone_number()
    elif choice==4:
        return
    else:
        print("Wrong input, Pls select a valid option.")
        run_again = input("Press any key to continue")

    
def update_name():
    mydb = mysql.connector.connect(host="localhost", user="root", passwd="passwor0", database="project")
    my_cursor = mydb.cursor()
    adm_num = int(input("Enter student's admission number: "))
    new_name = input("Enter the correct name: ")
    my_cursor.execute(f"update admission set student_name='{new_name}' where admission_num={adm_num}")
    mydb.commit()
    print("Name has been updated successfully!")


def update_address():
    mydb = mysql.connector.connect(host="localhost", user="root", passwd="passwor0", database="project")
    my_cursor = mydb.cursor()
    adm_num = int(input("Enter student's admission number: "))
    new_address = input("Enter the correct address: ")
    my_cursor.execute(f"update admission set address='{new_address}' where admission_num={adm_num}")
    mydb.commit()
    print("Address has been updated successfully!")
    

def update_phone_number():
    mydb = mysql.connector.connect(host="localhost", user="root", passwd="passwor0", database="project")
    my_cursor = mydb.cursor()
    adm_num = int(input("Enter student's admission number: "))
    new_phone_num = int(input("Enter the correct phone number: "))
    my_cursor.execute(f"update admission set phone_num={new_phone_num} where admission_num={adm_num}")
    mydb.commit()
    print("Phone number has been updated successfully!")
