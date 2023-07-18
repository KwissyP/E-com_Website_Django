from django_seed import Seed
from user.models import Role, User
from django.contrib.auth.hashers import make_password

def runConnexion():
    seeder = Seed.seeder()

    roles = [
        {'value': Role.ADMIN},
        {'value': Role.WEB},
        {'value': Role.MEMBER},
    ]
    
    for item in roles:
        seeder.add_entity(Role, 1, item)
    
    print(seeder.execute())

    users = [
        {'username': 'admin', 'email': 'admin@admin.com', 'password': make_password('1234'), 'role': Role.objects.get(value=Role.ADMIN), 'img_url' : 'https://sm.ign.com/ign_fr/cover/a/avatar-gen/avatar-generations_bssq.jpg'},
        {'username': 'web', 'email': 'web@web.com', 'password': make_password('1234'), 'role': Role.objects.get(value=Role.WEB), 'img_url' : 'https://static.vecteezy.com/ti/vecteur-libre/p3/3731316-web-icon-vector-line-on-white-background-image-for-web-presentation-logo-icon-symbol-gratuit-vectoriel.jpg'},
        {'username': 'member', 'email': 'member@member.com', 'password': make_password('1234'), 'role': Role.objects.get(value=Role.MEMBER), 'img_url' : 'https://accws.org/wp-content/uploads/2014/04/member-stamp.jpg'},
    ]
    
    for item in users:
        seeder.add_entity(User, 1, item)
    
    print(seeder.execute())
