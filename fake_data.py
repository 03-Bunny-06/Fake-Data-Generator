from rich.table import Table
from rich.console import Console

from faker import Faker 
fake = Faker()

def data(i):
    first = fake.first_name()
    last = fake.last_name()
    full_name = first + ' ' + last
    dob = fake.date_of_birth()
    phone = fake.phone_number()
    email = fake.email()
    cc_number = fake.credit_card_number()
    cc_provider = fake.credit_card_provider()
    company = fake.company()
    job = fake.job()
    address = fake.address()
    zip_code = fake.zipcode()
    city = fake.city()
    state = fake.state()
    country = fake.country()

    console = Console()
    table = Table(title=f'{i}: Fake Data')
    table.add_column('Full Name', justify='center', min_width=20)
    table.add_column('Date of Birth', justify='left', min_width=15)
    table.add_column('Phone', justify='left', min_width=15)
    table.add_column('E-mail', justify='left', min_width=20)
    table.add_column('Credit Card Number', justify='left', min_width=20)
    table.add_column('Credit Card Provider', justify='left', min_width=20)
    table.add_column('Company', justify='left', min_width=20)
    table.add_column('Job', justify='left', min_width=20)
    table.add_column('Address', justify='left', min_width=20)
    table.add_column('ZIP Code', justify='left', min_width=15)
    table.add_column('City', justify='left', min_width=15)
    table.add_column('State', justify='left', min_width=15)
    table.add_column('Country', justify='left', min_width=15)

    table.add_row(full_name, str(dob), str(phone), str(email), str(cc_number), cc_provider, company, job, address, str(zip_code), city, state, country)

    console.print(table)

rangee = int(input("No of fake data's: "))
for i in range(1,rangee+1):
    data(i)