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
