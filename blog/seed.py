from django_seed import Seed
from .models import CategoryArticle, Tag, Article
from user.models import User

def runBlog():
    seeder = Seed.seeder()

    # Création des catégories
    categories = ["Chaussures", "Accessoires", "Soin"]
    for category in categories:
        CategoryArticle.objects.create(category=category)
        
    # Création des tags
    tags = ["Sunglasses", "Luxe", "Montre", "Noir", "Sportswear", "White", "Casquette", "Rouge", "Grey", "Parfum", "Shampoing", "Cheveux", "Après-soleil", "Autobronzant"]
    for tag in tags:
        Tag.objects.create(tag=tag)
    
    articles = [
        {
            "title": "PRADA",
            "img": "https://img01.ztat.net/article/spp-media-p1/a8ff53630deb4a39b9d8b862c193c403/2f42863502e145c4b3a9344e5c9b0d07.jpg?imwidth=1800&filter=packshot",
            "description": "Design inspiration lorem ipsum dolor sit amet, consectetuer adipiscing elit. Morbi commodo, ipsum sed pharetra gravida, orci magna rhoncus neque, id pulvinar odio lorem non turpis. Nullam sit amet enim. Suspendisse id velit vitae ligula volutpat condimentum. Aliquam erat volutpat. Sed quis velit. Nulla facilisi. Nulla libero. Vivamus pharetra posuere sapien. Nam consectetuer. Sed aliquam, nunc eget euismod ullamcorper, lectus nunc ullamcorper orci, fermentum bibendum enim nibh eget ipsum. Nam consectetuer. Sed aliquam, nunc eget euismod ullamcorper, lectus nunc ullamcorper orci, fermentum bibendum enim nibh eget ipsum. Nulla libero. Vivamus pharetra posuere sapien.",
            "category": CategoryArticle.objects.get(category="Accessoires"),
            "tag": Tag.objects.filter(tag__in=["Sunglasses", "Luxe"]),
            "user": User.objects.get(username="admin"),
            "validate": True,
        },
        {
            "title": "VERSACE",
            "img": "https://img01.ztat.net/article/spp-media-p1/b12e1977952e3ec5844d5d5725b0a78a/ac8f737ba6bd40a1b0f5dcf35f40dfa4.jpg?imwidth=1800&filter=packshot",
            "description": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus et sagittis leo, ut malesuada purus. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus et sagittis leo, ut malesuada purus. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus et sagittis leo, ut malesuada purus.",
            "category": CategoryArticle.objects.get(category="Accessoires"),
            "tag": Tag.objects.filter(tag__in=["Sunglasses", "Luxe"]),
            "user": User.objects.get(username="admin"),
            "validate": True,
        },
        {
            "title": "G-Shock",
            "img": "https://img01.ztat.net/article/spp-media-p1/ac3288776098469bb5f42f75d7a7ec48/62b4a0d641294d07a73b5b9edf3383e7.jpg?imwidth=1800",
            "description": "Integer aliquet imperdiet odio a volutpat. Suspendisse potenti. Curabitur sit amet metus vitae ex finibus laoreet. Integer aliquet imperdiet odio a volutpat. Suspendisse potenti. Curabitur sit amet metus vitae ex finibus laoreet. Integer aliquet imperdiet odio a volutpat. Suspendisse potenti. Curabitur sit amet metus vitae ex finibus laoreet.",
            "category": CategoryArticle.objects.get(category="Accessoires"),
            "tag": Tag.objects.filter(tag__in=["Montre", "Noir"]),
            "user": User.objects.get(username="admin"),
            "validate": False,
        },
        {
            "title": "POLO RALPH LAUREN",
            "img": "https://img01.ztat.net/article/spp-media-p1/97377ff3ac1f384e85f74bea397f05a5/1c1e00746a3d40ea803965271da4ea83.jpg?imwidth=1800",
            "description": "Integer aliquet imperdiet odio a volutpat. Suspendisse potenti. Curabitur sit amet metus vitae ex finibus laoreet. Integer aliquet imperdiet odio a volutpat. Suspendisse potenti. Curabitur sit amet metus vitae ex finibus laoreet. Integer aliquet imperdiet odio a volutpat. Suspendisse potenti. Curabitur sit amet metus vitae ex finibus laoreet.",
            "category": CategoryArticle.objects.get(category="Accessoires"),
            "tag": Tag.objects.filter(tag__in=["Casquette", "Rouge"]),
            "user": User.objects.get(username="admin"),
            "validate": False,
        },
        {
            "title": "NIKE",
            "img": "https://img01.ztat.net/article/spp-media-p1/a7a6243dfd6c457c90cb4490b2e31385/e18c157281c54a199791476e4dfacff7.jpg?imwidth=1800",
            "description": "Integer aliquet imperdiet odio a volutpat. Suspendisse potenti. Curabitur sit amet metus vitae ex finibus laoreet. Integer aliquet imperdiet odio a volutpat. Suspendisse potenti. Curabitur sit amet metus vitae ex finibus laoreet. Integer aliquet imperdiet odio a volutpat. Suspendisse potenti. Curabitur sit amet metus vitae ex finibus laoreet.",
            "category": CategoryArticle.objects.get(category="Chaussures"),
            "tag": Tag.objects.filter(tag__in=["Sportswear", "White"]),
            "user": User.objects.get(username="admin"),
            "validate": False,
        },
        {
            "title": "ASICS",
            "img": "https://img01.ztat.net/article/spp-media-p1/b52734f26b0c48989934ab6e2cd7b76a/d754a0f03a8d4877bf58d4a168b4ac16.jpg?imwidth=1800",
            "description": "Integer aliquet imperdiet odio a volutpat. Suspendisse potenti. Curabitur sit amet metus vitae ex finibus laoreet. Integer aliquet imperdiet odio a volutpat. Suspendisse potenti. Curabitur sit amet metus vitae ex finibus laoreet. Integer aliquet imperdiet odio a volutpat. Suspendisse potenti. Curabitur sit amet metus vitae ex finibus laoreet.",
            "category": CategoryArticle.objects.get(category="Chaussures"),
            "tag": Tag.objects.filter(tag__in=["Sportswear", "Grey"]),
            "user": User.objects.get(username="admin"),
            "validate": False,
        },
        {
            "title": "VERSACE JEANS COUTURE",
            "img": "https://img01.ztat.net/article/spp-media-p1/deb5beb49e9145f88cdb5c576b9dd569/1971bf3ac4264f2fa6b9f2f10e48b4b1.jpg?imwidth=1800",
            "description": "Integer aliquet imperdiet odio a volutpat. Suspendisse potenti. Curabitur sit amet metus vitae ex finibus laoreet. Integer aliquet imperdiet odio a volutpat. Suspendisse potenti. Curabitur sit amet metus vitae ex finibus laoreet. Integer aliquet imperdiet odio a volutpat. Suspendisse potenti. Curabitur sit amet metus vitae ex finibus laoreet.",
            "category": CategoryArticle.objects.get(category="Chaussures"),
            "tag": Tag.objects.filter(tag__in=["Luxe", "White"]),
            "user": User.objects.get(username="admin"),
            "validate": False,
        },
        {
            "title": "AZZARO",
            "img": "https://img01.ztat.net/article/spp-media-p1/17e8c44ffa044ae1a34a3c19753ec1b2/22cdff201d2d423baded361498d4e949.jpg?imwidth=1800&filter=packshot",
            "description": "Integer aliquet imperdiet odio a volutpat. Suspendisse potenti. Curabitur sit amet metus vitae ex finibus laoreet. Integer aliquet imperdiet odio a volutpat. Suspendisse potenti. Curabitur sit amet metus vitae ex finibus laoreet. Integer aliquet imperdiet odio a volutpat. Suspendisse potenti. Curabitur sit amet metus vitae ex finibus laoreet.",
            "category": CategoryArticle.objects.get(category="Soin"),
            "tag": Tag.objects.filter(tag__in=["Parfum", "Luxe"]),
            "user": User.objects.get(username="admin"),
            "validate": False,
        },
        {
            "title": "KÉRASTASE",
            "img": "https://img01.ztat.net/article/spp-media-p1/adfc63bf844148b4be94e758c3a1a52b/52dfc11926894740a99741eb5e291d33.jpg?imwidth=1800&filter=packshot",
            "description": "Integer aliquet imperdiet odio a volutpat. Suspendisse potenti. Curabitur sit amet metus vitae ex finibus laoreet. Integer aliquet imperdiet odio a volutpat. Suspendisse potenti. Curabitur sit amet metus vitae ex finibus laoreet. Integer aliquet imperdiet odio a volutpat. Suspendisse potenti. Curabitur sit amet metus vitae ex finibus laoreet.",
            "category": CategoryArticle.objects.get(category="Soin"),
            "tag": Tag.objects.filter(tag__in=["Shampoing", "Cheveux"]),
            "user": User.objects.get(username="admin"),
            "validate": False,
        },
        {
            "title": "GARNIER",
            "img": "https://img01.ztat.net/article/spp-media-p1/0f3976f644b2412e90eb9d0eae2b7d4b/f7585462559c4aa5b57ace8c7b6daf58.jpg?imwidth=1800&filter=packshot",
            "description": "Integer aliquet imperdiet odio a volutpat. Suspendisse potenti. Curabitur sit amet metus vitae ex finibus laoreet. Integer aliquet imperdiet odio a volutpat. Suspendisse potenti. Curabitur sit amet metus vitae ex finibus laoreet. Integer aliquet imperdiet odio a volutpat. Suspendisse potenti. Curabitur sit amet metus vitae ex finibus laoreet.",
            "category": CategoryArticle.objects.get(category="Soin"),
            "tag": Tag.objects.filter(tag__in=["Après-soleil", "Autobronzant"]),
            "user": User.objects.get(username="admin"),
            "validate": False,
        },
    ]
    
    for art in articles:
        article = Article.objects.create(
            title=art["title"],
            img=art["img"],
            description=art["description"],
            category=art["category"],
            user=art["user"],
            validate=art["validate"],
        )
        article.tag.set(art["tag"])

    print("Seeding completed successfully!")