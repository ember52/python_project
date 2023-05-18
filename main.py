import datetime
import csv
from datetime import date

current_date = datetime.datetime.now().strftime("%d%m%Y")
current_working_file = f"Contact book_{current_date}.csv"


def user_selection():
    selection = input("please select if you want to : (create=1),(update=2), (delete=3) please select a number \n")
    if selection.isdigit():
        if int(selection) == 1:
            user_input()
        elif int(selection) == 2:
            user_update()
        elif int(selection) == 3:
            user_delete()
        else:
            print("wrong choice please choose from (1),(2),(3) \n")
            user_selection()

    else:
        print("please enter a valid choice \n")
        user_selection()


def restart_app():
    flag = 0
    while flag == 0:
        choice = input("would you like to do anything else?(Y/N) \n")
        if (choice == 'y') | (choice == 'Y'):
            user_selection()
            flag = 1
        elif (choice == 'n') | (choice == 'N'):
            print('thank you for using the app ! \n')
            flag = 1
        else:
            print("please enter a valid answer \n")
            flag = 0


def import_original_data():
    with open('Contact Book.csv', 'r') as file:
        reader = csv.reader(file)
        rows = list(reader)
        rows.append(row)
        with open(current_working_file, 'w', newline='') as file:
            adder = csv.writer(file)
            adder.writerows(rows)


def user_input():
    flag = 0
    contact_name = input("please enter the contact name: \n")
    contact_email = input("please enter the contact email: \n")
    while flag == 0:
        contact_number = input("please input the contact number: \n")
        if contact_number.isdigit():
            flag = 1
        else:
            print("please enter a correct contact \n")
            flag = 0

    contact_address = input("please enter the contact address: \n")
    insertion_date = datetime.datetime.now().strftime('%d-%m-%Y- %H:%M:%S')
    save_inputs(contact_name, contact_email, contact_number, contact_address, insertion_date)
    restart_app()


def save_inputs(contact_name, contact_email, contact_number, contact_address, insertion_date):
    import_original_data()
    with open(current_working_file, 'a', newline='') as file:
        adder = csv.writer(file)
        adder.writerow([contact_name, contact_email, contact_number, contact_address, insertion_date])
    print("your data has been successfully saved ! \n")


def user_update():
    flag = 0
    flag3 = 0
    while flag == 0:
        search_field = input("please choose field you want to update ( contact name = 1, contact email = 2, contact "
                             "number = 3,contact address = 4 ) : ")
        if search_field.isdigit():
            flag = 1
        else:
            print("please enter a valid choice \n")
            flag = 0

    if 0 < int(search_field) < 5:
        search_email = input("please enter the email of the contact to be updated: \n")
        with open(current_working_file, 'r') as file:
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
                        new_value = input("Please Enter New Value:  \n")
                        row[0] = new_value
                    elif int(search_field) == 2:
                        new_value = input("Please Enter New Value:  \n")
                        row[1] = new_value
                    elif int(search_field) == 3:
                        while flag3 == 0:
                            new_value = input("please input the new contact number: \n")
                            if new_value.isdigit():
                                flag3 = 1
                            else:
                                print("please enter a correct contact number ! \n")
                                flag3 = 0
                        row[2] = new_value
                    elif int(search_field) == 4:
                        new_value = input("Please Enter New Value: \n ")
                        row[3] = new_value
            with open(current_working_file, 'w', newline='') as file:
                writer = csv.writer(file)
                writer.writerows(rows)
            print("contacts list has been updated successfully \n")
            restart_app()
        else:
            print("please input a correct email ! \n")
            user_update()
    else:
        print("wrong input please try again \n")
        user_update()


def user_delete():
    search_email = input("Enter The Contact email You Want To Remove: \n ")
    with open(current_working_file, 'r') as file:
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
                with open(current_working_file, 'w', newline='') as file:
                    adder = csv.writer(file)
                    adder.writerows(rows)
        print("Contact Has Been  Deleted Successfully \n")
        restart_app()
    else:
        print("please enter a valid email ! \n")
        user_delete()


if __name__ == '__main__':
    user_selection()
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
