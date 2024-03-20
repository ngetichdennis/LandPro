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
