import admission
import student_data

print("\t\t..........................................................")
print("\t\t***********Welcome To School Management System************")
print("\t\t..........................................................")
print("\n\t\t****************Aster Public School*********************")
while True:
    print("1: Admission")
    print("2: Student Data")
    print("3: Fees Details")
    print("4: Exit")
    print("\t\t-----------------------------------------------------------")
    choice = int(input("Enter your choice 1-4: "))
    if choice==1:
        admission.ADM_MENU()
    elif choice==2:
        student_data.STU_MENU()
    # elif choice==3:
    #     fee_details.FEE_MENU()
    # elif choice==4:
    #     break
    # else:
    #     print("Wrong input, Pls select a valid option.")
    #     run_again = input("Press any key to continue")


    