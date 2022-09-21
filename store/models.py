from django.db import models

import time
import pandas as pd
from django.db import models
from django.urls import reverse


class Category(models.Model):
    productcategoryid = models.AutoField(blank=True, primary_key=True)
    category = models.CharField(db_column = 'name', max_length=50, blank=True, null=True)
    rowguid = models.CharField(max_length=100, blank=True, null=True)
    modifieddate = models.DateField(blank=True, null=True)

    def get_url(self):
        return reverse('product_by_category', args=[self.productcategoryid])

class PandasModelMixin(models.Model):
    class Meta:
        abstract = True

    @classmethod
    def as_dataframe(cls, queryset=None, field_list=None):
        t1 = time.time()

        if queryset is None:
            queryset = cls.objects.all()
        if field_list is None:
            field_list = [_field.name for _field in cls._meta._get_fields(reverse=False)]

        data = []
        [data.append([obj.serializable_value(column) for column in field_list]) for obj in queryset]

        columns = field_list

        df = pd.DataFrame(data, columns=columns)
        return df


class Detail(PandasModelMixin):
    product_name = models.CharField(max_length=50, blank=True, null=True)
    productid = models.IntegerField(blank=True, primary_key=True)
    description = models.CharField(max_length=5000, blank=True, null=True)
    quantity = models.IntegerField(blank=True, null=True)
    listprice = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    is_available = models.CharField(max_length=5, blank=True, null=True)
    images = models.CharField(max_length=50, blank=True, null=True)
    category = models.CharField(max_length=50, blank=True, null=True)
    modifieddate = models.DateField(blank=True, null=True)
    productcategoryid = models.IntegerField(blank=True, null=True)
    productsubcategoryid = models.IntegerField(blank=True, null=True)
    subcategory = models.CharField(max_length=50, blank=True, null=True)
    weight = models.FloatField(blank=True, null=True)
    productline = models.CharField(max_length=50, blank=True, null=True)
    class_field = models.CharField(db_column='class', max_length=50, blank=True, null=True) 
    style = models.CharField(max_length=50, blank=True, null=True)


    def attrs(self):
        for attr, value in self.__dict__.iteritems():
            yield attr, value


class Product(models.Model):
    subcategory = models.CharField(max_length=50, blank=True, null=True)
    productsubcategoryid = models.CharField(max_length=50, blank=True, primary_key=True)
    quantity = models.IntegerField(blank=True, null=True)
    is_available = models.CharField(max_length=5, blank=True, null=True)
    images = models.CharField(max_length=50, blank=True, null=True)
    category = models.CharField(max_length=50, blank=True, null=True) 
    modifieddate = models.DateField(blank=True, null=True)
    productcategoryid = models.IntegerField(blank=True, null=True)