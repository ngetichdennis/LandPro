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
