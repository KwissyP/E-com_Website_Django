from django_seed import Seed
from user.models import Role, User
from django.contrib.auth.hashers import make_password

def runConnexion():
    seeder = Seed.seeder()

    roles = [
        {'value': Role.ADMIN},
        {'value': Role.WEB},
        {'value': Role.STOCK},
        {'value': Role.MEMBER},
    ]
    
    for item in roles:
        seeder.add_entity(Role, 1, item)
    
    print(seeder.execute())

    users = [
        {'username': 'admin', 'email': 'admin@admin.com', 'password': make_password('1234'), 'role': Role.objects.get(value=Role.ADMIN), 'img_url' : 'https://toppng.com/uploads/preview/app-icon-set-login-icon-comments-avatar-icon-11553436380yill0nchdm.png'},
        {'username': 'web', 'email': 'web@web.com', 'password': make_password('1234'), 'role': Role.objects.get(value=Role.WEB), 'img_url' : 'https://toppng.com/uploads/preview/app-icon-set-login-icon-comments-avatar-icon-11553436380yill0nchdm.png'},
        {'username': 'stock', 'email': 'stock@stock.com', 'password': make_password('1234'), 'role': Role.objects.get(value=Role.STOCK), 'img_url' : 'https://toppng.com/uploads/preview/app-icon-set-login-icon-comments-avatar-icon-11553436380yill0nchdm.png'},
        {'username': 'member', 'email': 'member@member.com', 'password': make_password('1234'), 'role': Role.objects.get(value=Role.MEMBER), 'img_url' : 'https://png.pngtree.com/png-vector/20220709/ourmid/pngtree-businessman-user-avatar-wearing-suit-with-red-tie-png-image_5809521.png'},
    ]
    
    for item in users:
        seeder.add_entity(User, 1, item)
    
    print(seeder.execute())
