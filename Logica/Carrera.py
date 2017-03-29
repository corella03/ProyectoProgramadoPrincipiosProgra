class Student ():
    def __init__(self):
        self.name = ""
        self.lastName = ""
        self.identificationCard = ""
        self.address = ""
        self.phone = ""
        self.email = ""
    def DataStudent (self,nameEntry,lastNameEntry,identificationCardEntry,addressEntry,phoneEntry,emailEntry):
        self.name = nameEntry
        self.lastName = lastNameEntry
        self.identificationCard = identificationCardEntry
        self.address = addressEntry
        self.phone = phoneEntry
        self.email = emailEntry
        return nameEntry, lastNameEntry,identificationCardEntry,addressEntry,phoneEntry,emailEntry