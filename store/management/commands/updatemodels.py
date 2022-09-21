from django.core.management.base import BaseCommand
import pandas as pd
from store.models import Detail

class Command(BaseCommand):
    help = 'import booms'

    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        df = pd.read_csv('detail.csv')
        df['quantity'].fillna(0, inplace=True)
        for index, row in df.iterrows():
            models = Detail(product_name=row['productname'],
                            productid=row['productid'],
                            description=row['description'],
                            quantity=row['quantity'],
                            listprice=row['listprice'],
                            is_available=row['isavailable'],
                            images=row['images'],
                            category=row['category'],
                            modifieddate='2014-02-08',
                            productcategoryid=row['productcategoryid'],
                            productsubcategoryid=row['productsubcategoryid'],
                            subcategory=row['subcategory'],
                            weight=row['weight'],
                            productline=row['productline'],
                            class_field=row['class_type'],
                            style=row['style'],
                            )
            models.save()

