from models.owner import Owner
from models.property import Property
from models.taxassessment import TaxAssessment

def add_owner():
    name = input("Enter owner's name: ")
    contact = input("Enter owner's contact: ")
    identification_no=input("Enter owner's identification_no:")
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
        print(f"{property.id}. Property Location:{property.location} Property area:{property.area} Property History {property.property_history}  Property Owner{owner_name}")
def find_owner_by_name():
    name = input("Enter the owner's name: ")
    owner = Owner.find_by_name(name)
    print(owner) if owner else print(
        f'Owner {name} not found')
    
def find_owner_by_id():
    # use a trailing underscore not to override the built-in id function
    id_ = input("Enter the owner's id: ")
    owner = Owner.find_by_id(id_)
    print(owner) if owner else print(f'Owner {id_} not found')
def find_property_by_id():
    # use a trailing underscore not to override the built-in id function
    id_ = input("Enter the property's id: ")
    property = Property.find_by_id(id_)
    print(property) if property else print(f'Property {id_} not found')


def find_property_by_name():
    name = input("Enter the owner's name: ")
    owner = Owner.find_by_name(name)
    print(owner) if owner else print(
        f'Owner {name} not found')
def update_owner():
    id_ = input("Enter the owner's id: ")
    if owner := Owner.find_by_id(id_):
        try:
            name = input("Enter the owner's new name: ")
            owner.name = name
            contact = input("Enter the owner's new contact: ")
            owner.contact = contact

            owner.update()
            print(f'Success: {owner}')
        except Exception as exc:
            print("Error updating owner: ", exc)
    else:
        print(f'Owner {id_} not found')
    
def update_property():
    id_ = input("Enter the property's id: ")
    if property := Property.find_by_id(id_):
        try:
            location = input("Enter the property's new name: ")
            property.location = location
            area = input("Enter the property's new area: ")
            property.area = area

            property.update()
            print(f'Success: {property}')
        except Exception as exc:
            print("Error updating property: ", exc)
    else:
        print(f'Property {id_} not found')
def delete_owner():
    id_ = input("Enter the owner's id: ")
    if owner := Owner.find_by_id(id_):
        owner.delete()
        print(f'Owner {id_} deleted')
    else:
        print(f'Owner {id_} not found')
        
def delete_property():
    id_ = input("Enter the property's id: ")
    if property := Property.find_by_id(id_):
        property.delete()
        print(f'Property {id_} deleted')
    else:
        print(f'Property {id_} not found')
        
def find_properties_by_owner_name():
    owner_name = input("Enter the owner's name: ")
    owner = Owner.find_by_name(owner_name)
    
    if owner:
        properties = Property.find_by_owner_id(owner.id)
        if properties:
            print(f"Properties owned by {owner_name}:")
            for prop in properties:
                print(f"Property Location:{prop.location}, {prop.area} square meters, Property History: {prop.property_history}")
        else:
            print(f"No properties found for {owner_name}.")
    else:
        print(f"Owner {owner_name} not found.")
        
def find_taxassessment_by_id():
    # use a trailing underscore not to override the built-in id function
    id_ = input("Enter the taxassessment's id: ")
    taxassessment = TaxAssessment.find_by_id(id_)
    print( taxassessment) if  taxassessment else print(f' Taxassessment {id_} not found')
    
def list_all_taxassessment():
    taxs = TaxAssessment.get_all()
    for tax in taxs:
        owner = Owner.find_by_id(tax.owner_id)
        property= Property.find_by_id(tax.property_id)
        if owner and  property :
            owner_name = owner.name
            property_location= property.location
        else:
            owner_name = "Unknown Owner"
            property_location="Unknown Property"
        print(f" Tax assessment for {tax.id}. Property owned by {owner_name} located at{property_location} was assessed on {tax.assessment_date}.It has a value of {tax.assessed_value} and the property tax status is {tax.payment_status}")

def add_taxassessment():
    property_id = input("Enter property's ID: ")
    owner_id = input("Enter owner's ID: ")
    assessment_date=input("Enter assessment date YYYY-MM-DD: ")
    assessed_value=float(input("Enter the Assesed Value: "))
    tax_rate=float(input("Enter the Tax Rate (%/100): "))
    payment_status=input("Enter Payment Status(paid/not paid: ")
    try:
        new_taxassessment = TaxAssessment.create(property_id,owner_id,assessment_date,assessed_value,tax_rate,payment_status)
        print(f"Tax Assessment added successfully:{new_taxassessment}")
        
    except Exception as exc:
        print("Error adding the tax assessment", exc)
        
def delete_taxassessment():
    id_ = input("Enter the Tax Assessment's id: ")
    if taxassessment := TaxAssessment.find_by_id(id_):
        taxassessment.delete()
        print(f'Tax Assessment {id_} deleted')
    else:
        print(f'Tax Assessment {id_} not found')
        
def update_taxassessment():
    id_ = input("Enter the tax assessment's id: ")
    if taxassessment := TaxAssessment.find_by_id(id_):
        try:
            property_id = input("Enter the property's ID: ")
            taxassessment.property_id = property_id
            owner_id = input("Enter the owner's ID: ")
            taxassessment.owner_id = owner_id
            new_assessment_date = input('Enter the new assessment date YYYY-MM-DD: ')
            taxassessment.assessment_date = new_assessment_date
            new_assessed_value= float(input('Enter the new Assesed Value: ')) 
            taxassessment.assessed_value=new_assessed_value
            new_tax_rates=float(input('Enter the new Tax rate(%/100): '))
            taxassessment.tax_rates=new_tax_rates
            new_payment_status=input('Enter the new Payment status(paid/not paid): ')
            taxassessment.payment_status=new_payment_status
            taxassessment.update()
            print(f'Success: {taxassessment}')
        except Exception as exc:
            print("Error updating tax assessment: ", exc)
    else:
        print(f'Tax asessment {id_} not found')



