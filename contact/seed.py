from django_seed import Seed
from .models import Contact

def runContact():
    seeder = Seed.seeder()

    contacts = [
        {
        'location': 'Wonder Street, USA, New York',
        'phone': '+01 321 654 214',
        'email': 'hello@xton.com',
        'fax': '+123456789',
        },
    ]

    for item in contacts:
        seeder.add_entity(Contact, 1, item)
    print(seeder.execute())