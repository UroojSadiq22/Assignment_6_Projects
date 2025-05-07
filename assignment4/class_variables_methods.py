# Assignment:
# Create a class Bank with a class variable bank_name. Add a class method change_bank_name(cls, name) that allows changing the bank name. Show that it affects all instances.

class Bank:
    bank_name = "UBL Bank"

    def __init__(self, user_name):
        self.user_name = user_name

    @classmethod
    def change_bank_name(cls, name):
        cls.bank_name = name

    def display_bank_name(self):
        print(f"User Name: {self.user_name}, Bank Name: {self.bank_name}")


# Create instances of the Bank class
bank1 = Bank("Alina")
bank2 = Bank("Bareera")

bank1.display_bank_name()
bank2.display_bank_name() 

print("\nChanging bank name...\n")
Bank.change_bank_name("HBL Bank")

bank1.display_bank_name()
bank2.display_bank_name()
    
