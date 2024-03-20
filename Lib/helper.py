from models.owner import Owner
from models.property import Property

def add_owner():
    name = input("Enter owner's name: ")
    contact = input("Enter owner's contact: ")
    identification_no=input("Enter owner's identification_no")
    try:
        new_owner = Owner.create(name,contact,identification_no)
        print(f"Owner added successfully:{new_owner}")
        
    except Exception as exc:
        print("Error adding the owner", exc)
    
def add_property():
    location = input("Enter the property's location: ")
    area = input("Enter the property's area in square metres: ")
    property_history=input("Enter property's property_history:")
    owner_id=input("Enter the property's onwner ID")
    try:
        new_property= Property.create(location, area,property_history,owner_id)
        print(f'Property added successfully: {new_property}')
    except Exception as exc:
        print("Error creating property: ", exc)
        
def list_all_owners():
    owners = Owner.get_all()
    for owner in owners:
        print(f"{owner.id}: {owner.name} {owner.contact} {owner.identification_no}")

def list_all_properties():
    properties = Property.get_all()
    for property in properties:
        owner = Owner.find_by_id(property.owner_id)
        if owner:
            owner_name = owner.name
        else:
            owner_name = "Unknown Owner"
        print(f"{property.id}: {property.location} {property.area} {property.property_history}  {owner_name}")


