import os
import django
import csv
import sys

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "freshez.settings")
django.setup()

from user.models import Allergy
from product.models import Product, ProductPurchaseMethod, PurchaseMethod, ProductAllergy

CSV_PATH_PRODUCTS = './CSV_Product_Allergy.csv'

with open(CSV_PATH_PRODUCTS) as in_file:
    data_reader = csv.reader(in_file)
    next(data_reader, None)
    for row in data_reader:
        allergy_instance = Allergy.objects.get(id=row[0])
        product_instance = Product.objects.get(id=row[1])
        ProductAllergy.objects.create(
            allergy=allergy_instance,
            product=product_instance
        )
    print("Done")
