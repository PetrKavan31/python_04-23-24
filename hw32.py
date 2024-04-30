# HW32
# Module 10 / part 1
# Task 1

# The user inputs a set of numbers from the keyboard.
# The received numbers should be saved in a list (the type of
# list is selected based on the task below). After this, display
# a menu offering the user the following items:
# 1. Add a new number to the list (if such a number exists
# in the list, inform the user about it and do not add the
# number).
# 2. Delete all occurrences of the number from the list (the user
# inputs a number to be deleted).
# 3. Show the list contents (show the list from the beginning
# or the end based on the user’s choice).
# 4. Check if the list contains this value.
# 5. Replace the value in the list (the user decides whether to
# replace only the first occurrence or all occurrences).
# The action is performed based on the user’s choice, and
# the menu displays again.


def add_number(num, num_list):
    if num in num_list:
        print("The number already exists in the list.")
    else:
        num_list.append(num)
        print("Number added successfully.")


def delete_number(num, num_list):
    while num in num_list:
        num_list.remove(num)
    print("All occurrences of the number have been deleted.")


def show_list(order, num_list):
    if order.upper() == "B":
        print(num_list)
    else:
        print(num_list[::-1])


def check_value(num, num_list):
    if num in num_list:
        print("The number exists in the list.")
    else:
        print("The number does not exist in the list.")


def replace_number(num, new_num, num_list, replace_all):
    if replace_all.upper() == "Y":
        for i in range(len(num_list)):
            if num_list[i] == num:
                num_list[i] = new_num
    else:
        num_list[num_list.index(num)] = new_num
    print("Number replaced successfully.")


def display_menu():
    numbers = input_number()
    menu = """
  Choose number 1-6:

  1. Add a new number to the list:
  2. Delete all occurrences of the number from the list
  3. Show the list contents
  4. Check if the list contains this value
  5. Replace the value in the list
  6. Exit
  """
    while True:
        print(menu)
        choice = int(input("Enter your choice: "))

        if choice == 1:
            num = int(input("Enter the number to add: "))
            add_number(num, numbers)

        elif choice == 2:
            num = int(input("Enter the number to delete: "))
            delete_number(num, numbers)

        elif choice == 3:
            order = input("Do you want to display the list from the beginning or the end? (B/E): ")
            show_list(order, numbers)

        elif choice == 4:
            num = int(input("Enter the number to check: "))
            check_value(num, numbers)

        elif choice == 5:
            num = int(input("Enter the number to replace: "))
            new_num = int(input("Enter the new number: "))
            replace_all = input("Do you want to replace all occurrences? (Y/N): ")
            replace_number(num, new_num, numbers, replace_all)

        elif choice == 6:
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 6.")


def input_number():
    # Asking user for a list of integers
    user_input = input("Enter a list of integers separated by spaces: ")
    int_list = [int(item) for item in user_input.split()]
    return int_list


display_menu()