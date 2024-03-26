from models.owner import Owner
from models.property import Property
from models.taxassessment import TaxAssessment

def seed_database():

    # Create owners
    Owner.create_table()
    Owner.create(name="Dennis Kipkirui", contact="1234567890", identification_no="ABC123")
    Owner.create(name="Ngetich Kipkirui", contact="0987654321", identification_no="XYZ789")
    
# Create properties
    Property.create_table()
    Property.create(location="Main St", area=1000, property_history="Good condition", owner_id=1)
    Property.create(location="Ngomeni St", area=1500, property_history="Needs renovation", owner_id=2)
# Create tax assessments
    TaxAssessment.create_table()
    TaxAssessment.create(property_id=1, owner_id=1, assessment_date="2024-03-22", assessed_value=100000, tax_rates=0.05, payment_status="Paid")
    TaxAssessment.create(property_id=2, owner_id=2, assessment_date="2024-03-22", assessed_value=150000, tax_rates=0.06, payment_status="Not Paid")
    print("Database seeded successfully.")

if __name__ == "__main__":
    seed_database()


