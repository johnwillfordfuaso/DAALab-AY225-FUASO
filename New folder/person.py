class Person:
    def __init__(self, id, first_name, last_name):
        self.id = int(id)
        self.first_name = first_name.strip()
        self.last_name = last_name.strip()
    
    def __repr__(self):
        return f"{self.id:<12} {self.first_name:<20} {self.last_name:<20}"
    
    def __str__(self):
        return self.__repr__()
