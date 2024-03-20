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

