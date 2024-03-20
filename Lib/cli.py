from helper import add_owner, add_property, list_all_owners, list_all_properties

def display_menu():
    print("\nWelcome to Property Management System")
    print("1. Add Owner")
    print("2. Add Property")
    print("3. List All Owners")
    print("4. List All Properties")
    print("5. Exit")

def main():
    while True:
        display_menu()
        choice = input("Enter your choice: ")
        if choice == "1":
            add_owner()
        elif choice == "2":
            add_property()
        elif choice == "3":
            list_all_owners()
        elif choice == "4":
            list_all_properties()
        elif choice == "5":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()
