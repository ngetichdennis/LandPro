from helper import add_owner, add_property, list_all_owners, list_all_properties, find_owner_by_name,find_property_by_name,find_owner_by_id,find_property_by_id,update_owner, update_property,delete_owner,delete_property,find_properties_by_owner_name,find_taxassessment_by_id,list_all_taxassessment,add_taxassessment,delete_taxassessment,update_taxassessment


def display_menu():
    print("\nWelcome to LandPro, a Property Management System")
    print("1. Manage Owners")
    print("2. Manage Properties")
    print("3. Tax assessment Manager")
    print("4. Find Information")
    print("5. Exit")

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
    
def display_taxassessment_menu():
    print("\nTax Assessment Manager\n")
    print("1. List All Taxassessment information")
    print("2. Add Tax assessment information.")
    print("3. Update Tax assessment information.")
    print("4. Remove Tax assessment information")
    print("5. Return to Main Menu.")
def display_find_menu():
    print("\nFind Information")
    print("1. Find Owner by name")
    print("2. Find Owner by ID")
    print("3. Find Property by ID")
    print("4. Find properties owned by a  specific owner")
    print("5.Find Tax Assessment by ID")
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
        
        elif choice =="3":
            while True:
                display_taxassessment_menu()
                taxassessment_choice=input("Enter your choice: ")
                if taxassessment_choice=="1":
                    list_all_taxassessment()
                elif taxassessment_choice=="2":
                    add_taxassessment()
                elif taxassessment_choice=="3":
                    update_taxassessment()
                elif taxassessment_choice=="4":
                    delete_taxassessment()
                elif taxassessment_choice=="5":
                    break
                else:
                    ("Invalid Choice.The value shoulf range from 1 to 5")
                    
        elif choice == "4":
            while True:
                display_find_menu()
                find_choice = input("Enter your choice: ")
                if find_choice == "1":
                    find_owner_by_name()
                elif find_choice == "2":
                    find_owner_by_id()
                elif find_choice == "3":
                    find_property_by_id()
                elif find_choice == "4":
                    find_properties_by_owner_name()
                elif find_choice=="5":
                    find_taxassessment_by_id()
                elif find_choice == "6":
                    break
                else:
                    print("Invalid choice. Please enter a number between 1 and 6.")
        elif choice == "5":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    main()
