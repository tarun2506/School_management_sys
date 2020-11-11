import mysql.connector

def STU_MENU():
    while True:
        print("1: Add Student Details")
        print("2: Show Student Details")
        print("3: Search Student Details")
        print("4: Delete Student Details")
        print("5: Update Student Details")
        print("6: Exit")
        print("\t\t-----------------------------------------------------------")
        choice=int(input("Enter your choice 1-6: "))
        if choice==1:
            add_details()
        elif choice==2:
            show_student_details()
        elif choice==3:
            search_student_details()
        elif choice==4:
            delete_student_details()
        elif choice==5:
            update_student_details()
        elif choice==6:
            return
        else:
            print("Wrong input, Pls select a valid option.")
            run_again = input("Press any key to continue: ")
        
        
#Defining the functions for certain tasks:

def add_details():
    try:
        mydb = mysql.connector.connect(host="localhost", user="root", passwd="passwor0", database="project")
        my_cursor = mydb.cursor()
        session=input("Enter academic session(eg,2021-2022): ")
        student_name=input("Enter student name: ")
        student_class= int(input("Enter student class: "))
        student_class_section = input("Enter section: ")
        student_class_rollnum = int(input("Enter student roll number: "))
        sub1= input("Enter subject 1: ")
        sub2= input("Enter subject 2: ")
        sub3= input("Enter subject 3: ")

        query = f"insert into student(session,name,class,section,roll_num,sub1,sub2,sub3) VALUES('{session}', '{student_name}', {student_class}, '{student_class_section}', {student_class_rollnum}, '{sub1}', '{sub2}', '{sub3}')"

        my_cursor.execute(query)
        mydb.commit()
        mydb.close()
        my_cursor.close()
        print("Details have been pushed to the student table successfully!")

    except:
        print("Error")

def show_student_details():
    mydb = mysql.connector.connect(host="localhost", user="root", passwd="passwor0", database="project")
    my_cursor = mydb.cursor()
    my_cursor.execute("select * from student")
    data = my_cursor.fetchall()
    for row in data:
        print(row)

def search_student_details():
    mydb = mysql.connector.connect(host="localhost", user="root", passwd="passwor0", database="project")
    my_cursor = mydb.cursor()
    roll_num = int(input("Enter student's roll number: "))
    my_cursor.execute(f"select * from student where roll_num={roll_num}")
    data = my_cursor.fetchall()
    print(data)

def delete_student_details():
    mydb = mysql.connector.connect(host="localhost", user="root", passwd="passwor0", database="project")
    my_cursor = mydb.cursor()
    roll_num = int(input("Enter student's roll number: "))
    my_cursor.execute(f"delete from student where roll_num={roll_num}")
    mydb.commit()
    print("Details have been deleted successfully!")

def update_student_details():
    # mydb = mysql.connector.connect(host="localhost", user="root", passwd="passwor0", database="project")
    # my_cursor = mydb.cursor()
    # Options for Updation:
    print("1: Update session")
    print("2: Update name")
    print("3: Update class")
    print("4: Update section")
    print("5: Update roll number")
    print("6: Update sub1")
    print("7: Update sub2")
    print("8: Update sub3")
    print("9: Return to main menu")
    choice=int(input("Enter your choice 1-9: "))
    if choice==1:
        update_session()
    elif choice==2:
        update_name()
    elif choice==3:
        update_class()
    elif choice==4:
        update_section()
    elif choice==5:
        update_roll_number()
    elif choice==6:
        update_sub1()
    elif choice==7:
        update_sub2()
    elif choice==8:
        update_sub3()
    elif choice==9:
        return
    else:
        print("Wrong input, Pls select a valid option.")
        run_again = input("Press any key to continue")


def update_session():
    mydb = mysql.connector.connect(host="localhost", user="root", passwd="passwor0", database="project")
    my_cursor = mydb.cursor()
    roll_num = int(input("Enter student's roll number: "))
    new_session = input("Enter correct session: ")
    my_cursor.execute(f"update student set session='{new_session}' where roll_num={roll_num}")
    mydb.commit()
    print("Session has been updated successfully!")

def update_name():
    mydb = mysql.connector.connect(host="localhost", user="root", passwd="passwor0", database="project")
    my_cursor = mydb.cursor()
    roll_num = int(input("Enter student's roll number: "))
    new_name = input("Enter correct name: ")
    my_cursor.execute(f"update student set name='{new_name}' where roll_num={roll_num}")
    mydb.commit()
    print("Name has been updated successfully!")

def update_class():
    mydb = mysql.connector.connect(host="localhost", user="root", passwd="passwor0", database="project")
    my_cursor = mydb.cursor()
    roll_num = int(input("Enter student's roll number: "))
    new_class = int(input("Enter correct class: "))
    my_cursor.execute(f"update student set class={new_class} where roll_num={roll_num}")
    mydb.commit()
    print("Class has been updated successfully!")

def update_section():
    mydb = mysql.connector.connect(host="localhost", user="root", passwd="passwor0", database="project")
    my_cursor = mydb.cursor()
    roll_num = int(input("Enter student's roll number: "))
    new_section = input("Enter correct section: ")
    my_cursor.execute(f"update student set section='{new_section}' where roll_num={roll_num}")
    mydb.commit()
    print("Section has been updated successfully!")

def update_roll_number():
    mydb = mysql.connector.connect(host="localhost", user="root", passwd="passwor0", database="project")
    my_cursor = mydb.cursor()
    roll_num = int(input("Enter student's roll number: "))
    new_roll_num = int(input("Enter correct roll number: "))
    my_cursor.execute(f"update student set roll_num={new_roll_num} where roll_num={roll_num}")
    mydb.commit()
    print("Roll number has been updated successfully!")

def update_sub1():
    mydb = mysql.connector.connect(host="localhost", user="root", passwd="passwor0", database="project")
    my_cursor = mydb.cursor()
    roll_num = int(input("Enter student's roll number: "))
    new_sub1 = input("Enter correct sub1: ")
    my_cursor.execute(f"update student set sub1='{new_sub1}' where roll_num={roll_num}")
    mydb.commit()
    print("Sub1 has been updated successfully!")

def update_sub2():
    mydb = mysql.connector.connect(host="localhost", user="root", passwd="passwor0", database="project")
    my_cursor = mydb.cursor()
    roll_num = int(input("Enter student's roll number: "))
    new_sub2 = input("Enter correct sub2: ")
    my_cursor.execute(f"update student set sub2='{new_sub2}' where roll_num={roll_num}")
    mydb.commit()
    print("Sub2 has been updated successfully!")


def update_sub3():
    mydb = mysql.connector.connect(host="localhost", user="root", passwd="passwor0", database="project")
    my_cursor = mydb.cursor()
    roll_num = int(input("Enter student's roll number: "))
    new_sub3 = input("Enter correct sub3: ")
    my_cursor.execute(f"update student set sub3='{new_sub3}' where roll_num={roll_num}")
    mydb.commit()
    print("Sub3 has been updated successfully!")