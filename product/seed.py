from django_seed import Seed
from .models import Category, Product

def runProduct():
    seeder = Seed.seeder()
    
    categories = [
        {'value': 'Chemises'},
        {'value': 'Sweats à capuche'},
        {'value': 'T-Shirts'},
        {'value': 'Tricots'},
        {'value': 'Vestes'},
    ]

    for item in categories:
        seeder.add_entity(Category, 1, item)
    
    print(seeder.execute())
    
    
    #----------------------------------------------------------------
    
    products = [
        {
            'img1': 'https://fr.arte-antwerp.com/cdn/shop/products/01062022_arte_ss23_ECOM_33417_2048x1891.jpg?v=1678186616', 
            'img2': 'https://fr.arte-antwerp.com/cdn/shop/products/01062022_arte_ss23_ECOM_33419_2048x1891.jpg?v=1678186616', 
            'img3': 'https://fr.arte-antwerp.com/cdn/shop/products/01062022_arte_ss23_ECOM_33423_2048x1891.jpg?v=1678186616',
            'description' : 'Le pull Klee Logo est la pièce décontractée et tricotée parfaite pour toute garde-robe. Fabriqué en coton de qualité supérieure, ce modèle de tous les jours offre confort et style. Ce pull se décline dans un bleu clair vibrant et arbore un logo Arte sur le devant.',
            'name': 'KLEE LOGO SWEATER - LIGHT BLUE/LAKE BLUE',
            'category': Category.objects.all()[3],
            'price': 130,
            'promo': 30,
            'stock': {
                'S': 2,
                'M': 2,
                'L': 2,
                'XL': 2,
                'XXL' : 2,
            },
        },
        {
            'img1': 'https://fr.arte-antwerp.com/cdn/shop/products/01062022_arte_ss23_ECOM_34810_2048x1891.jpg?v=1674210315', 
            'img2': 'https://fr.arte-antwerp.com/cdn/shop/products/01062022_arte_ss23_ECOM_34815_2048x1891.jpg?v=1674210315', 
            'img3': 'https://fr.arte-antwerp.com/cdn/shop/products/01062022_arte_ss23_ECOM_34815_2048x1891.jpg?v=1674210315',
            'description' : 'Le pull Klee Multi offre un équilibre sans effort entre audace et confort. Son design coloré et rayé crée une esthétique vibrante et accrocheuse. Fabriqué en coton de qualité supérieure, ce pull est respirant et doux au toucher.',
            'name': 'KLEE MULTI SWEATER - MULTICOLOR',
            'category': Category.objects.all()[3],
            'price': 130,
            'promo': 20,
            'stock': {
                'S': 4,
                'M': 8,
                'L': 6,
                'XL': 1,
                'XXL': 2,
            },
        },
        {
            'img1': 'https://fr.arte-antwerp.com/cdn/shop/products/01062022_arte_ss23_ECOM_33758_2048x1891.jpg?v=1678187752', 
            'img2': 'https://fr.arte-antwerp.com/cdn/shop/products/01062022_arte_ss23_ECOM_33756_2048x1891.jpg?v=1678187752', 
            'img3': 'https://fr.arte-antwerp.com/cdn/shop/products/01062022_arte_ss23_ECOM_33763_2048x1891.jpg?v=1678187752',
            'description' : "Le pull rayé en tricot est le complément idéal de votre garde-robe décontractée. Fabriqué en coton de qualité supérieure, ce pull est doux au toucher et sa coupe décontractée assure un confort maximal. Son design est défini par les rayures blanches qui s'étendent sur le corps rouge du vêtement. Enfin, le logo Arte est brodé en blanc sur le côté gauche de la poitrine.",
            'name': 'STRIPED KNIT SWEATER - RED/WHITE',
            'category': Category.objects.all()[3],
            'price': 150,
            'promo': 15,
            'stock': {
                'S': 3,
                'M': 8,
                'L': 7,
                'XL': 4,
                'XXL': 6,
            },
        },
        {
            'img1': 'https://fr.arte-antwerp.com/cdn/shop/products/01062022_arte_ss23_ECOM_32877_2048x1891.jpg?v=1676468581', 
            'img2': 'https://fr.arte-antwerp.com/cdn/shop/products/01062022_arte_ss23_ECOM_32879_2048x1891.jpg?v=1676468581', 
            'img3': 'https://fr.arte-antwerp.com/cdn/shop/products/01062022_arte_ss23_ECOM_32882_2048x1891.jpg?v=1676468581',
            'description' : "Le T-shirt Tzéry Stripes visualise les codes de style d'Arte pour l'automne/hiver 2023. Le T-shirt se présente sous la forme de rayures multicolores qui s'enroulent autour du corps du vêtement. Confectionné à partir d'un coton léger et de qualité supérieure, le T-shirt présente une encolure légèrement plus haute et est coupé dans une coupe décontractée.",
            'name': 'TÉRY STRIPES T-SHIRT - BLACK',
            'category': Category.objects.all()[2],
            'price': 75,
            'promo': 0,
            'stock': {
                'S': 2,
                'M': 8,
                'L': 7,
                'XL': 7,
                'XXL': 9,
            },
        },
        {
            'img1': 'https://fr.arte-antwerp.com/cdn/shop/products/01062022_arte_ss23_ECOM_34552_2048x1891.jpg?v=1676468608', 
            'img2': 'https://fr.arte-antwerp.com/cdn/shop/products/01062022_arte_ss23_ECOM_34564_2048x1891.jpg?v=1676468608', 
            'img3': 'https://fr.arte-antwerp.com/cdn/shop/products/01062022_arte_ss23_ECOM_34557_2048x1891.jpg?v=1676468608',
            'description' : "Le T-shirt Tzéry Stripes visualise les codes de style d'Arte pour l'automne/hiver 2023. Le T-shirt se présente sous la forme de rayures multicolores qui s'enroulent autour du corps du vêtement. Confectionné à partir d'un coton léger et de qualité supérieure, le T-shirt présente une encolure légèrement plus haute et est coupé dans une coupe décontractée.",
            'name': 'TÉRY STRIPES T-SHIRT - BLUE',
            'category': Category.objects.all()[2],
            'price': 75,
            'promo': 0,
            'stock': {
                'S': 2,
                'M': 3,
                'L': 4,
                'XL': 5,
                'XXL': 6,
            },
        },
        {
            'img1': 'https://fr.arte-antwerp.com/cdn/shop/products/01062022_arte_ss23_ECOM_33114_2048x1891.jpg?v=1673456896', 
            'img2': 'https://fr.arte-antwerp.com/cdn/shop/products/01062022_arte_ss23_ECOM_33118_2048x1891.jpg?v=1673456895', 
            'img3': 'https://fr.arte-antwerp.com/cdn/shop/products/01062022_arte_ss23_ECOM_33122_2048x1891.jpg?v=1673456895',
            'description' : "Le T-shirt Taut Embroi Logo en noir est un article de base de tous les jours qui s'intègre parfaitement à toute garde-robe. Ce t-shirt présente l'interprétation de cette saison du logo en forme de cœur, signature d'Arte, brodé en blanc sur le côté gauche de la poitrine. Il présente une encolure légèrement plus haute et est coupé dans une coupe décontractée.",
            'name': 'TAUT EMBROI HEART LOGO T-SHIRT - BLACK',
            'category': Category.objects.all()[2],
            'price': 65,
            'promo': 20,
            'stock': {
                'S': 4,
                'M': 8,
                'L': 6,
                'XL': 1,
                'XXL': 2,
            },
        },
        {
            'img1': 'https://fr.arte-antwerp.com/cdn/shop/products/01062022_arte_ss23_ECOM_32058_2048x1891.jpg?v=1678185650', 
            'img2': 'https://fr.arte-antwerp.com/cdn/shop/products/01062022_arte_ss23_ECOM_32069_2048x1891.jpg?v=1678185650', 
            'img3': 'https://fr.arte-antwerp.com/cdn/shop/products/01062022_arte_ss23_ECOM_32062_2048x1891.jpg?v=1678185650',
            'description' : "Affrontez les éléments avec la veste Jeremey. Fabriquée en nylon de première qualité, cette veste se décline dans un coloris contrasté bleu clair et crème et comporte deux poches latérales ainsi que deux poches de poitrine, toutes deux zippées. Le logo Arte est brodé en crème sur le côté gauche de la poitrine. Enfin, la veste est dotée d'une ceinture élastique qui peut être ajustée pour garantir la coupe souhaitée.",
            'name': 'JEREMY JACKET - LIGHT BLUE/CREAM',
            'category': Category.objects.all()[4],
            'price': 230,
            'promo': 50,
            'stock': {
                'S': 4,
                'M': 8,
                'L': 6,
                'XL': 1,
                'XXL': 2,
            },
        },
        {
            'img1': 'https://fr.arte-antwerp.com/cdn/shop/products/01062022_arte_ss23_ECOM_33143_2048x1891.jpg?v=1673624905', 
            'img2': 'https://fr.arte-antwerp.com/cdn/shop/products/01062022_arte_ss23_ECOM_33145_2048x1891.jpg?v=1674830988', 
            'img3': 'https://fr.arte-antwerp.com/cdn/shop/products/01062022_arte_ss23_ECOM_33147_2048x1891.jpg?v=1674830988',
            'description' : "La veste Jackson allover s'inspire de l'esprit Bauhaus qui règne dans toute la collection printemps-été. Confectionnée en pur coton, la veste en denim boutonnée se présente dans une teinte crème et présente un logo Arte saisonnier allover en rouge. Elle est dotée de deux poches latérales, de deux poches poitrine et d'une étiquette tissée de la marque sur la poitrine gauche.",
            'name': 'JACKSON ALLOVER LOGO JACKET - RED/WHITE',
            'category': Category.objects.all()[4],
            'price': 185,
            'promo': 0,
            'stock': {
                'S': 4,
                'M': 8,
                'L': 6,
                'XL': 1,
                'XXL': 2,
            },
        },
        {
            'img1': 'https://fr.arte-antwerp.com/cdn/shop/products/01062022_arte_ss23_ECOM_33193_2048x1891.jpg?v=1673877727', 
            'img2': 'https://fr.arte-antwerp.com/cdn/shop/products/01062022_arte_ss23_ECOM_33196_2048x1891.jpg?v=1673877727', 
            'img3': 'https://fr.arte-antwerp.com/cdn/shop/products/01062022_arte_ss23_ECOM_33198_2048x1891.jpg?v=1673877727',
            'description' : "La veste Jones Colorblock s'inspire de l'esprit Bauhaus qui règne dans toute la collection printemps-été. Confectionnée en pur coton, la veste en denim boutonnée se présente dans une combinaison de couleurs gris nuageux et crème. Elle est dotée de deux poches latérales, de deux poches poitrine et d'une étiquette tissée de marque sur la poitrine gauche. La veste se marie parfaitement avec le pantalon Jones Colorblock.",
            'name': 'JONES COLORBLOCK JACKET - CREAM/NIMBUS CLOUD',
            'category': Category.objects.all()[4],
            'price': 195,
            'promo': 0,
            'stock': {
                'S': 4,
                'M': 8,
                'L': 6,
                'XL': 1,
                'XXL': 2,
            },
        },
        {
            'img1': 'https://fr.arte-antwerp.com/cdn/shop/products/01062022_arte_ss23_ECOM_33073_2048x1891.jpg?v=1679336584', 
            'img2': 'https://fr.arte-antwerp.com/cdn/shop/products/01062022_arte_ss23_ECOM_33076_2048x1891.jpg?v=1679336584', 
            'img3': 'https://fr.arte-antwerp.com/cdn/shop/products/01062022_arte_ss23_ECOM_330801_2048x1891.jpg?v=1679336584',
            'description' : "Le sweat à capuche Henny Multi se présente sous la forme d'un demi-zip avec un motif à blocs de couleur crème et bleu lac. Le sweat à capuche présente le logo Arte brodé en bleu lac sur le côté gauche de la poitrine ainsi que deux poches à couture latérale. Fabriqué en coton épais de qualité supérieure, il est doux au toucher et présente une coupe décontractée.",
            'name': 'HENNY MULTI HOODIE - CREAM/LAKE BLUE',
            'category': Category.objects.all()[1],
            'price': 130,
            'promo': 10,
            'stock': {
                'S': 4,
                'M': 8,
                'L': 6,
                'XL': 1,
                'XXL': 2,
            },
        },
        {
            'img1': 'https://fr.arte-antwerp.com/cdn/shop/products/01062022_arte_ss23_ECOM_32790_2048x1891.jpg?v=1678180765', 
            'img2': 'https://fr.arte-antwerp.com/cdn/shop/products/01062022_arte_ss23_ECOM_32793_2048x1891.jpg?v=1678180765', 
            'img3': 'https://fr.arte-antwerp.com/cdn/shop/products/01062022_arte_ss23_ECOM_32801_2048x1891.jpg?v=1678180765',
            'description' : "Le sweat à capuche Hannes Logo est un complément décontracté à votre garde-robe. Ce sweat à capuche est disponible dans un coloris blanc polyvalent et présente la version de cette saison du logo Arte brodé au centre de la poitrine. Fabriqué en coton épais de première qualité, ce sweat à capuche a une coupe décontractée pour un mélange de confort et de style.",
            'name': 'HANNES LOGO HOODIE - WHITE',
            'category': Category.objects.all()[1],
            'price': 120,
            'promo': 0,
            'stock': {
                'S': 3,
                'M': 5,
                'L': 3,
                'XL': 6,
                'XXL': 8,
            },
        },
        {
            'img1': 'https://fr.arte-antwerp.com/cdn/shop/products/01062022_arte_ss23_ECOM_34433_2048x1891.jpg?v=1679336613', 
            'img2': 'https://fr.arte-antwerp.com/cdn/shop/products/01062022_arte_ss23_ECOM_34445_2048x1891.jpg?v=1679336613', 
            'img3': 'https://fr.arte-antwerp.com/cdn/shop/products/01062022_arte_ss23_ECOM_34437_2048x1891.jpg?v=1679336613',
            'description' : "Le sweat à capuche Henny Multi se présente sous la forme d'un demi-zip avec un design en blocs de couleur gris et marine. Le sweat à capuche présente le logo Arte brodé en bleu marine sur le côté gauche de la poitrine, ainsi que deux poches à couture latérale. Fabriqué en coton épais de qualité supérieure, il est doux au toucher et présente une coupe décontractée.",
            'name': 'HENNY MULTI HOODIE - GREY/NAVY',
            'category': Category.objects.all()[1],
            'price': 130,
            'promo': 20,
            'stock': {
                'S': 3,
                'M': 6,
                'L': 9,
                'XL': 1,
                'XXL': 2,
            },
        },
        {
            'img1': 'https://fr.arte-antwerp.com/cdn/shop/products/01062022_arte_ss23_ECOM_33449_2048x1891.jpg?v=1676388532', 
            'img2': 'https://fr.arte-antwerp.com/cdn/shop/products/01062022_arte_ss23_ECOM_33452_2048x1891.jpg?v=1676388531', 
            'img3': 'https://fr.arte-antwerp.com/cdn/shop/products/01062022_arte_ss23_ECOM_33454_2048x1891.jpg?v=1676388532',
            'description' : "La chemise imprimée Stockton visualise la direction artistique de cette saison. Cette chemise présente un imprimé abstrait sur l'ensemble du corps dans une combinaison de couleurs bleu clair et blanc. Fabriquée en coton de qualité supérieure, la chemise est munie d'une fermeture à boutons régulière sur toute la longueur.",
            'name': 'STOCKTON PRINT SHIRT - LIGHT BLUE/WHITE',
            'category': Category.objects.all()[0],
            'price': 120,
            'promo': 0,
            'stock': {
                'S': 1,
                'M': 3,
                'L': 9,
                'XL': 10,
                'XXL': 12,
            },
        },
        {
            'img1': 'https://fr.arte-antwerp.com/cdn/shop/products/01062022_arte_ss23_ECOM_33054_2048x1891.jpg?v=1678969813', 
            'img2': 'https://fr.arte-antwerp.com/cdn/shop/products/01062022_arte_ss23_ECOM_33059_2048x1891.jpg?v=1678969813', 
            'img3': 'https://fr.arte-antwerp.com/cdn/shop/products/01062022_arte_ss23_ECOM_33062_2048x1891.jpg?v=1678969813',
            'description' : "La pochette Peter Detail chemise est un look saisonnier sur nos chemises à manches courtes. Fabriqué en coton de première qualité, le chemise Il est de couleur bleu lac et comporte deux poches 3D surpiquées sur l'épaule. poitrine avant. Le site chemise se présente avec un col montant et des boutons cachés sur le devant pour la fermeture. ",
            'name': 'PETER DETAIL POCKET SHIRT - LAKE BLUE',
            'category': Category.objects.all()[0],
            'price': 120,
            'promo': 0,
            'stock': {
                'S': 4,
                'M': 6,
                'L': 9,
                'XL': 3,
                'XXL': 8,
            },
        },
        {
            'img1': 'https://fr.arte-antwerp.com/cdn/shop/products/01062022_arte_ss23_ECOM_35260_2048x1891.jpg?v=1674210581', 
            'img2': 'https://fr.arte-antwerp.com/cdn/shop/products/01062022_arte_ss23_ECOM_35275_2048x1891.jpg?v=1674210581', 
            'img3': 'https://fr.arte-antwerp.com/cdn/shop/products/01062022_arte_ss23_ECOM_35265_2048x1891.jpg?v=1674210581',
            'description' : "La chemise Scottie Print reprend l'esprit Bauhaus qui anime toute la collection printemps-été. Imprimée d'un motif graphique fort dans une couleur marine et verte, la chemise est une véritable pièce d'exception. La chemise Scott a une coupe décontractée et un col décontracté. Elle se termine par des boutons.",
            'name': 'SCOTTIE PRINT SHIRT - NAVY/GREEN',
            'category': Category.objects.all()[0],
            'price': 120,
            'promo': 0,
            'stock': {
                'S': 3,
                'M': 5,
                'L': 4,
                'XL': 12,
                'XXL': 3,
            },
        },
    ]
    
    for item in products:
        seeder.add_entity(Product, 1, item)
    print(seeder.execute())
    
        
