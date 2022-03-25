from faker import Faker
fake = Faker()

class BaseContact:
    def __init__(self, first_name, last_name, phone, email):
        self.first_name = first_name
        self.last_name = last_name
        self.phone = phone
        self.email = email

        self.label_lenght = len(first_name) + len(last_name) + 1
        
    def contact(self):
        return f'Wybieram numer {self.phone} i dzwonię do {self.first_name} {self.last_name}.'  

class BusinessContact(BaseContact):
    def __init__(self, occupation, company, company_phone, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.occupation = occupation
        self.company = company
        self.company_phone = company_phone

    def contact(self):
        return f'Wybieram numer {self.company_phone} i dzwonię do {self.first_name} {self.last_name}.'  


def create_contacts(type, quantity):
    contacts= []
    for i in range(quantity):
        if type == 'Base':
            person = BaseContact(
                first_name=fake.first_name(),
                last_name=fake.last_name(),
                phone=fake.phone_number(),
                email=fake.email()
            )
            contacts.append(person)
        if type == 'Business':
            person = BusinessContact(
                first_name=fake.first_name(),
                last_name=fake.last_name(),
                phone=fake.phone_number(),
                email=fake.email(),
                occupation=fake.job(),
                company=fake.company(),
                company_phone=fake.phone_number()
            )
            contacts.append(person)
    return contacts
