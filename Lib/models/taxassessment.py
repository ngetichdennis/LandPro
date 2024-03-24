# lib/models/tax_assessment.py

from models.__init__ import CURSOR, CONN

class TaxAssessment:

    # Dictionary of objects saved to the database.
    all = {}

    def __init__(self, property_id, owner_id, assessment_date, assessed_value, tax_rates, payment_status, id=None):
        self.id = id
        self.property_id = property_id
        self.owner_id = owner_id
        self.assessment_date = assessment_date
        self.assessed_value = assessed_value
        self.tax_rates = tax_rates
        self.payment_status = payment_status

    def __str__(self):
        return f"Tax Assessment for Property ID {self.property_id} - Owner ID {self.owner_id} - Date: {self.assessment_date} - Value: {self.assessed_value}"

    @classmethod
    def create_table(cls):
        """ Create a new table to persist the attributes of tax assessment instances """
        sql = """
            CREATE TABLE IF NOT EXISTS tax_assessments (
            id INTEGER PRIMARY KEY,
            property_id INTEGER,
            owner_id INTEGER,
            assessment_date TEXT,
            assessed_value REAL,
            tax_rates REAL,
            payment_status TEXT,
            FOREIGN KEY (property_id) REFERENCES properties(id),
            FOREIGN KEY (owner_id) REFERENCES owners(id))
        """
        CURSOR.execute(sql)
        CONN.commit()
        
    @classmethod
    def create(cls, property_id, owner_id, assessment_date, assessed_value, tax_rates, payment_status):
        """Create a new tax assessment entry in the database."""
        sql = """
            INSERT INTO tax_assessments (property_id, owner_id, assessment_date, assessed_value, tax_rates, payment_status)
            VALUES (?, ?, ?, ?, ?, ?)
        """
        CURSOR.execute(sql, (property_id, owner_id, assessment_date, assessed_value, tax_rates, payment_status))
        CONN.commit()

        tax_assessment_id = CURSOR.lastrowid
        return cls(property_id, owner_id, assessment_date, assessed_value, tax_rates, payment_status, id=tax_assessment_id)

    @classmethod
    def get_all(cls):
        """Retrieve all tax assessments from the database."""
        sql = """
            SELECT * FROM tax_assessments
        """
        CURSOR.execute(sql)
        rows = CURSOR.fetchall()
        return [cls.instance_from_db(row) for row in rows]

    @classmethod
    def instance_from_db(cls, row):
        """Create a TaxAssessment instance from a database row."""
        # Check the dictionary for  existing instance using the row's primary key
        taxassessment = cls.all.get(row[0])
        if taxassessment:
            # ensure attributes match row values in case local instance was modified
            taxassessment.property_id = row[1]
            taxassessment.owner_id = row[2]
            taxassessment.assessment_date=row[3]
            taxassessment.assessed_value = row[4]
            taxassessment.tax_rates = row[5]
            taxassessment.payment_status = row[6]
            
        else:
            # not in dictionary, create new instance and add to dictionary
            taxassessment = cls(row[1], row[2], row[3], row[4],row[5],row[6])
            taxassessment.id = row[0]
            cls.all[taxassessment.id] = taxassessment
        return taxassessment

    @classmethod
    def find_by_id(cls, id):
        """Find a tax assessment by its ID."""
        sql = """
            SELECT * FROM tax_assessments WHERE id = ?
        """
        CURSOR.execute(sql, (id,))
        row = CURSOR.fetchone()
        return cls.instance_from_db(row) if row else None