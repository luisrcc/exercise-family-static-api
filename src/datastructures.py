
"""
update this file to implement the following already declared methods:
- add_member: Should add a member to the self._members list
- delete_member: Should delete a member from the self._members list
- update_member: Should update a member from the self._members list
- get_member: Should return a member from the self._members list
"""
from random import randint

class FamilyStructure:
    def __init__(self, last_name):
        self.last_name = last_name
        
        # example list of members
        self._members = [{
        'id' : self._generateId(), 
        'name': 'John', 
        'last_name' : self.last_name, 
        'age': 33, 
        'lucky_number': [7, 13, 22]
        },
        {
        'id' : self._generateId(), 
        'name': 'Jane', 
        'last_name' : self.last_name, 
        'age': 35, 
        'lucky_number': [10, 14, 3]
        },
        {
        'id' : self._generateId(), 
        'name': 'Jimmy', 
        'last_name' : self.last_name, 
        'age': 5, 
        'lucky_number': [1]
        }]

    # read-only: Use this method to generate random members ID's when adding members into the list
    def _generateId(self):
        return randint(0, 99999999)

    def add_member(self, member):
        adding_member = {}

        adding_member['id']=self._generateId()

        adding_member['name']=str(member['name'])

        adding_member['last_name']=self.last_name

        adding_member['age']=int(member['age'])

        adding_member['lucky_number']=member['lucky_number']

        self._members.append(adding_member)

        return None

    def delete_member(self, id):
        for member in self._members:
           if self._members[member]['id']== id:
               self._members.pop(member)
               return self._members

        return None

    def get_member(self, id):
        for member in self._members:
            if self._members[member]['id']== id:
                return member

    # this method is done, it returns a list with all the family members
    def get_all_members(self):
        return self._members
