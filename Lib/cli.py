from helper import add_owner, add_property, list_all_owners, list_all_properties, find_owner_by_name,find_property_by_name,find_owner_by_id,find_property_by_id,update_owner, update_property,delete_owner, delete_property,find_properties_by_owner_name

def display_menu():
    print("\nWelcome to LandPro, a Property Management System")
    print("1. Manage Owners")
    print("2. Manage Properties")
    print("3. Find Information")
    print("4. Exit")

def display_owner_menu():
    print("\nManage Owners")
    print("1. Add Owner")
    print("2. List All Owners")
    print("3. Update Owner")
    print("4. Delete Owner")
    print("5. Return to main menu")

def display_property_menu():
    print("\nManage Properties")
    print("1. Add Property")
    print("2. List All Properties")
    print("3. Update Property")
    print("4. Delete Property")
    print("5. Return to main menu")

def display_find_menu():
    print("\nFind Information")
    print("1. Find Owner by name")
    print("2. Find Property by name")
    print("3. Find Owner by ID")
    print("4. Find Property by ID")
    print("5. Find properties owned by an owner")
    print("6. Return to main menu")

def main():
    while True:
        display_menu()
        choice = input("Enter your choice: ")
        if choice == "1":
            while True:
                display_owner_menu()
                owner_choice = input("Enter your choice: ")
                if owner_choice == "1":
                    add_owner()
                elif owner_choice == "2":
                    list_all_owners()
                elif owner_choice == "3":
                    update_owner()
                elif owner_choice == "4":
                    delete_owner()
                elif owner_choice == "5":
                    break
                else:
                    print("Invalid choice. Please enter a number between 1 and 5.")
        elif choice == "2":
            while True:
                display_property_menu()
                property_choice = input("Enter your choice: ")
                if property_choice == "1":
                    add_property()
                elif property_choice == "2":
                    list_all_properties()
                elif property_choice == "3":
                    update_property()
                elif property_choice == "4":
                    delete_property()
                elif property_choice == "5":
                    break
                else:
                    print("Invalid choice. Please enter a number between 1 and 5.")
        elif choice == "3":
            while True:
                display_find_menu()
                find_choice = input("Enter your choice: ")
                if find_choice == "1":
                    find_owner_by_name()
                elif find_choice == "2":
                    find_property_by_name()
                elif find_choice == "3":
                    find_owner_by_id()
                elif find_choice == "4":
                    find_property_by_id()
                elif find_choice == "5":
                    find_properties_by_owner_name()
                elif find_choice == "6":
                    break
                else:
                    print("Invalid choice. Please enter a number between 1 and 6.")
        elif choice == "4":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    main()
