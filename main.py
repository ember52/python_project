# This is a sample Python script.
import datetime
import csv


# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
def user_selection():
    selection = int(input("please select if you want to : (create=1),(update=2), (delete=3) please select a number"))
    if selection == 1:
        user_input()
    elif selection == 2:
        user_update()
    elif selection == 3:
        user_delete()
    else:
        print("wrong choice please choose from (1),(2),(3)")
        user_selection()


def user_input():
    flag = 0
    flag2 = 0
    contact_name = input("please enter the contact name:")
    contact_email = input("please enter the contact email:")
    while flag == 0:
        contact_number = input("please input the contact number:")
        if contact_number.isdigit():
            flag = 1
        else:
            print("please enter a correct contact")
            flag = 0

    contact_address = input("please enter the contact address:")
    insertion_date = datetime.datetime.now().strftime('%d-%m-%Y- %H:%M:%S')
    save_inputs(contact_name, contact_email, contact_number, contact_address, insertion_date)
    while flag2 == 0:
        restart_app = input("would you like to do anything else?(Y/N)")
        if (restart_app == 'y') | (restart_app == 'Y'):
            user_selection()
            flag2 = 1
        elif (restart_app == 'n') | (restart_app == 'N'):
            print('thank you for using the app !')
            flag2 = 1
        else:
            print("please enter a valid answer")


def save_inputs(contact_name, contact_email, contact_number, contact_address, insertion_date):
    with open('Contact Book.csv', 'a', newline='') as file:
        adder = csv.writer(file)
        adder.writerow([contact_name, contact_email, contact_number, contact_address, insertion_date])
    print("your data has been successfully saved !")


def user_update():
    flag = 0
    flag2 = 0
    flag3 = 0
    while flag == 0:
        search_field = input("please choose field you want to update ( contact name = 1, contact email = 2, contact "
                             "number = 3,contact address = 4 ) : ")
        if search_field.isdigit():
            flag = 1
        else:
            print("please enter a valid choice")
            flag = 0

    if 0 < int(search_field) < 5:
        search_email = input("please enter the email of the contact to be updated:")
        with open('Contact Book.csv', 'r') as file:
            reader = csv.reader(file)
            rows = list(reader)
        for row in rows:
            if row[1] == search_email:
                validation = 1
                break
            else:
                validation = 0
        if validation == 1:
            for row in rows:
                if row[1] == search_email:
                    if int(search_field) == 1:
                        new_value = input("Please Enter New Value: ")
                        row[0] = new_value
                    elif int(search_field) == 2:
                        new_value = input("Please Enter New Value: ")
                        row[1] = new_value
                    elif int(search_field) == 3:
                        while flag3 == 0:
                            new_value = input("please input the new contact number:")
                            if new_value.isdigit():
                                flag3 = 1
                            else:
                                print("please enter a correct contact number !")
                                flag3= 0
                        row[2] = new_value
                    elif int(search_field) == 4:
                        new_value = input("Please Enter New Value: ")
                        row[3] = new_value
            with open('Contact Book.csv', 'w', newline='') as file:
                writer = csv.writer(file)
                writer.writerows(rows)
            print("contacts list has been updated successfully")
            while flag2 == 0:
                restart_app = input("would you like to do anything else?(Y/N)")
                if (restart_app == 'y') | (restart_app == 'Y'):
                    user_selection()
                    flag2 = 1
                elif (restart_app == 'n') | (restart_app == 'N'):
                    print('thank you for using the app !')
                    flag2 = 1
                else:
                    print("please enter a valid answer")
        else:
            print("please input a correct email !")
            user_update()
    else:
        print("wrong input please try again")
        user_update()


def user_delete():
    search_email = input("Enter The Contact email You Want To Remove: ")
    flag = 0
    with open('Contact Book.csv', 'r') as file:
        reader = csv.reader(file)
        rows = list(reader)
    for row in rows:
        if row[1] == search_email:
            validation = 1
            break
        else:
            validation = 0
    if validation == 1:
        for row in rows:
            if row[1] == search_email:
                rows.remove(row)
                with open('Contact Book.csv', 'w', newline='') as file:
                    adder = csv.writer(file)
                    adder.writerows(rows)
        print("Contact Has Been  Deleted Successfully")
        while flag == 0:
            restart_app = input("would you like to do anything else?(Y/N)")
            if (restart_app == 'y') | (restart_app == 'Y'):
                user_selection()
                flag = 1
            elif (restart_app == 'n') | (restart_app == 'N'):
                print('thank you for using the app !')
                flag = 1
            else:
                print("please enter a valid answer")
    else:
        print("please enter a valid email !")
        user_delete()




if __name__ == '__main__':
    user_selection()
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
