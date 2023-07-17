import django
django.setup()

from user.seed import runConnexion
from product.seed import runProduct
from blog.seed import runBlog
from contact.seed import runContact


if __name__ == '__main__':
    runConnexion()
    runProduct()
    runBlog()
    runContact()
