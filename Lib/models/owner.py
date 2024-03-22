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
        
    def __str__(self):
        return f"(Owner: {self.name}  - Contact: {self.contact}  ID:{self.identification_no})"


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
        
    def delete(self):
        """Delete the table row corresponding to the current Owner instance,
        delete the dictionary entry, and reassign id attribute"""

        sql = """
            DELETE FROM owners
            WHERE id = ?
        """

        CURSOR.execute(sql, (self.id,))
        CONN.commit()

        # Delete the dictionary entry using id as the key
        del type(self).all[self.id]

        # Set the id to None
        self.id = None

    @classmethod
    def instance_from_db(cls, row):
        """Return a Owner object having the attribute values from the table row."""

        # Check the dictionary for an existing instance using the row's primary key
        owner = cls.all.get(row[0])
        if owner:
            # ensure attributes match row values in case local instance was modified
            owner.name = row[1]
            owner.contact = row[2]
            owner.identification_no = row[3]
        else:
            # not in dictionary, create new instance and add to dictionary
            owner = cls(row[1], row[2],row[3])
            owner.id = row[0]
            cls.all[owner.id] = owner
        return owner

    @classmethod
    def get_all(cls):
        """Return a list containing a Owner object per row in the table"""
        sql = """
            SELECT *
            FROM owners
        """

        rows = CURSOR.execute(sql).fetchall()

        return [cls.instance_from_db(row) for row in rows]

    @classmethod
    def find_by_id(cls, id):
        """Return a Owner object corresponding to the table row matching the specified primary key"""
        sql = """
            SELECT *
            FROM owners
            WHERE id = ?
        """

        row = CURSOR.execute(sql, (id,)).fetchone()
        return cls.instance_from_db(row) if row else None

    @classmethod
    def find_by_name(cls, name):
        """Return a Owner object corresponding to first table row matching specified name"""
        sql = """
            SELECT *
            FROM owners
            WHERE name is ?
        """

        row = CURSOR.execute(sql, (name,)).fetchone()
        return cls.instance_from_db(row) if row else None

    def properties(self):
        """Return list of properties associated with current owner"""
        from models.property import Property
        sql = """
            SELECT * FROM properties
            WHERE owner_id = ?
        """
        CURSOR.execute(sql, (self.id,),)

        rows = CURSOR.fetchall()
        return [
            Property.instance_from_db(row) for row in rows
        ]


