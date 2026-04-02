import fileinput
import sys
import os

# Set the working directory to the script's directory
os.chdir(os.path.dirname(os.path.abspath(__file__)))


def contents(file_name):
    line_number = 1
    for line in file_name:
        print(f"{line_number}: {line.strip()}")
        line_number += 1


def deletion():
    try:
        delete_line_number = int(input("\nEnter the line number to delete: "))
    except ValueError:
        print("Invalid input. Please enter a number.")
        sys.exit()

    for line_number, line in enumerate(
        fileinput.input("items.todo_list.txt", inplace=1), start=1
    ):
        if line_number == delete_line_number:
            continue
        sys.stdout.write(line)
    print(f"\nLine {delete_line_number} deleted successfully.")


ask = input("Do you wanna add todos? (y/n):").lower()

if ask == "y":
    with open("items.todo_list.txt", "a") as file_a:
        ask = input("\nEnter a new task:")
        file_a.write(f"{ask}\n")
else:
    print("\nOkay!")

ask = input("\nDo you wanna see your todos? (y/n):").lower()

if ask == "y":
    try:
        with open("items.todo_list.txt", "r") as file_r:
            print("\nThe Todos are:\n")
            contents(file_r)
    except Exception:
        print("Add todo's to see them.")
else:
    print("\nOkay!")

ask = input("\nDo you wanna delete any of the todos? (y/n):")
print()

if ask == "y":
    try:
        with open("items.todo_list.txt", "r") as file_d:
            contents(file_d)
        deletion()
        print()
        with open("items.todo_list.txt", "r") as file_r:
            contents(file_r)
    except Exception:
        print("Add todo's to delete them.")
