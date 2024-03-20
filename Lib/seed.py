from models.owner import Owner
from models.property import Property

def seed_database():

    # Create owners
    Owner.create_table()
    Owner.create(name="John Doe", contact="1234567890", identification_no="ABC123")
    Owner.create(name="Jane Smith", contact="0987654321", identification_no="XYZ789")
    
# Create properties
    Property.create_table()
    Property.create(location="123 Main St", area=1000, property_history="Good condition", owner_id=1)
    Property.create(location="456 Elm St", area=1500, property_history="Needs renovation", owner_id=2)

    print("Database seeded successfully.")

if __name__ == "__main__":
    seed_database()


