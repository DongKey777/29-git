import os
import django
import csv
import sys

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "freshez.settings")
django.setup()

from user.models import User

CSV_PATH_PRODUCTS = './CSV_User.csv'

with open(CSV_PATH_PRODUCTS) as in_file:
    data_reader = csv.reader(in_file)
    next(data_reader, None)
    for row in data_reader:
        User.objects.create(
            email=row[0],
            password=row[1],
            name=row[2],
            nickname=row[3],
            phone=row[4],
            birth=row[5],
            sex=row[6]
        )
    print("Done")