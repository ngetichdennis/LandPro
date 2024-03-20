# lib/models/department.py
from models.__init__ import CURSOR, CONN

class Owner:

    # Dictionary of objects saved to the database.
    all = {}

    def __init__(self, name ,contact,identification_no, id=None):
        self.id = id
        self.name = name
        self.contact=contact
        self.identification_no=identification_no


    @classmethod
    def create_table(cls):
        """ Create a new table to persist the attributes of owner instances """
        sql = """
            CREATE TABLE IF NOT EXISTS owners (
            id INTEGER PRIMARY KEY,
            name TEXT,
            contact INT,
            identification_no INT)
        """
        CURSOR.execute(sql)
        CONN.commit()

    @classmethod
    def drop_table(cls):
        """ Drop the table that persists Owner instances """
        sql = """
            DROP TABLE IF EXISTS owners;
        """
        CURSOR.execute(sql)
        CONN.commit()
    
    
    def save(self):
        """ Insert a new row with the name,contact and identification_no values of the current Owner instance.
        Update object id attribute using the primary key value of new row.
        Save the object in local dictionary using table row's PK as dictionary key"""
        sql = """
            INSERT INTO owners (name,contact,identification_no)
            VALUES (?, ?, ?)
        """

        CURSOR.execute(sql, (self.name,self.contact,self.identification_no))
        CONN.commit()

        self.id = CURSOR.lastrowid
        type(self).all[self.id] = self

    @classmethod
    def create(cls,name,contact,identification_no):
        """ Initialize a new Owner instance and save the object to the database """
        owner = cls(name,contact,identification_no)
        owner.save()
        return owner

    def update(self):
        """Update the table row corresponding to the current owner instance."""
        sql = """
            UPDATE owners
            SET name = ?, contact = ?, identification_no = ?
            WHERE id = ?
        """
        CURSOR.execute(sql, (self.name,self.contact,self.identification_no, self.id))
        CONN.commit()

