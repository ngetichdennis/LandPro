from models.owner import Owner
from models.property import Property

def seed_database():

    # Create owners
    Owner.create_table()
    Owner.create(name="John Doe", contact="1234567890", identification_no="ABC123")
    Owner.create(name="Jane Smith", contact="0987654321", identification_no="XYZ789")

