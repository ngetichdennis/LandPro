from helper import add_owner, add_property, list_all_owners, list_all_properties, find_owner_by_name,find_property_by_name,find_owner_by_id,find_property_by_id,update_owner, update_property,delete_owner, delete_property

def display_menu():
    print("\nWelcome to Property Management System")
    print("1. Add Owner")
    print("2. Add Property")
    print("3. List All Owners")
    print("4. List All Properties")
    print("5. Find Owner by name")
    print("6. Find property by name")
    print("7. Find owner by ID")
    print("8. Find Properties by ID")
    print("9. Update Owners")
    print("10. Update Properties")
    print("11. Delete Owners")
    print("12. Delete Properties")
    print("13. Exit")

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
        elif choice =="5":
            find_owner_by_name()
        elif choice =="6":
            find_property_by_name()
        elif choice =="7":
            find_owner_by_id()
        elif choice=="8":
            find_property_by_id()
        elif choice =="9":
            update_owner()
        elif choice=="10":
            update_property()
        elif choice=="11":
            delete_owner()
        elif  choice=="12":
            delete_property()
        elif choice == "13":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()
