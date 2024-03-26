# lib/models/employee.py
from models.__init__ import CURSOR, CONN
from models.owner import Owner

class Property:

    # Dictionary of objects saved to the database.
    all = {}

    def __init__(self, location, area, property_history,owner_id, id=None):
        self.id = id
        self.location = location
        self.area = area
        self.property_history=property_history
        self.owner_id = owner_id
        
    def __str__(self):
        return f"(Property location is {self.location} has an area of {self.area} square Metres.The property has{self.property_history} history and it is owned by {self.owner_id})"

        
    @classmethod
    def create_table(cls):
        """ Create a new table to persist the attributes of property instances """
        sql = """
            CREATE TABLE IF NOT EXISTS properties (
            id INTEGER PRIMARY KEY,
            location TEXT,
            area INT,
            property_history TEXT,
            owner_id INTEGER,
            FOREIGN KEY (owner_id) REFERENCES owners(id))
        """
        CURSOR.execute(sql)
        CONN.commit()

    @classmethod
    def drop_table(cls):
        """ Drop the table that persists property instances """
        sql = """
            DROP TABLE IF EXISTS properties;
        """
        CURSOR.execute(sql)
        CONN.commit()

    def save(self):
        """ Insert a new row with the location, area,property_history and owner id values of the current property object.
        Update object id attribute using the primary key value of new row.
        Save the object in local dictionary using table row's PK as dictionary key"""
        sql = """
                INSERT INTO properties (location, area, property_history, owner_id)
                VALUES (?, ?, ?, ?)
        """

        CURSOR.execute(sql, (self.location, self.area, self.property_history, self.owner_id))
        CONN.commit()

        self.id = CURSOR.lastrowid
        type(self).all[self.id] = self
        
    def update(self):
        """Update the table row corresponding to the current property instance."""
        sql = """
            UPDATE properties
            SET location = ?, area = ?, property_history = ?, owner_id = ?
            WHERE id = ?
        """
        CURSOR.execute(sql, (self.location, self.area,self.property_history,
                            self.owner_id, self.id))
        CONN.commit()

    def delete(self):
        """Delete the table row corresponding to the current propertyinstance,
        delete the dictionary entry, and reassign id attribute"""

        sql = """
            DELETE FROM properties
            WHERE id = ?
        """

        CURSOR.execute(sql, (self.id,))
        CONN.commit()

        # Delete the dictionary entry using id as the key
        del type(self).all[self.id]

        # Set the id to None
        self.id = None

    @classmethod
    def create(cls, location, area, property_history, owner_id):
        """ Initialize a new Employee instance and save the object to the database """
        property = cls(location, area, property_history, owner_id)
        property.save()
        return property
    
    
    @classmethod
    def instance_from_db(cls, row):
        """Return an property object having the attribute values from the table row."""

        # Check the dictionary for  existing instance using the row's primary key
        property = cls.all.get(row[0])
        if property:
            # ensure attributes match row values in case local instance was modified
            property.location = row[1]
            property.area = row[2]
            property.property_history=row[3]
            property.owner_id = row[4]
        else:
            # not in dictionary, create new instance and add to dictionary
            property = cls(row[1], row[2], row[3], row[4])
            property.id = row[0]
            cls.all[property.id] = property
        return property

    @classmethod
    def get_all(cls):
        """Return a list containing one property object per table row"""
        sql = """
            SELECT *
            FROM properties
        """

        rows = CURSOR.execute(sql).fetchall()

        return [cls.instance_from_db(row) for row in rows]

    @classmethod
    def find_by_id(cls, id):
        """Return Properties object corresponding to the table row matching the specified primary key"""
        sql = """
            SELECT *
            FROM properties
            WHERE id = ?
        """

        row = CURSOR.execute(sql, (id,)).fetchone()
        return cls.instance_from_db(row) if row else None
    @classmethod
    def find_by_location(cls, location):
        """Return Properties object corresponding to the table row matching the specified primary key"""
        sql = """
            SELECT *
            FROM properties
            WHERE location = ?
        """

        row = CURSOR.execute(sql, (location,)).fetchone()
        return cls.instance_from_db(row) if row else None
    

    @classmethod
    def find_by_name(cls, name):
        """Return Properties object corresponding to first table row matching specified name"""
        sql = """
            SELECT *
            FROM properties
            WHERE name is ?
        """

        row = CURSOR.execute(sql, (name,)).fetchone()
        return cls.instance_from_db(row) if row else None
    
    @classmethod
    def find_by_owner_id(cls, owner_id):
        """Return a list of properties owned by the specified owner ID."""
        sql = """
            SELECT *
            FROM properties
            WHERE owner_id = ?
        """

        rows = CURSOR.execute(sql, (owner_id,)).fetchall()

        return [cls.instance_from_db(row) for row in rows]




