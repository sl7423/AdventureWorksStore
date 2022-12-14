# Generated by Django 3.2.5 on 2022-09-18 14:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('productcategoryid', models.AutoField(primary_key=True, serialize=False)),
                ('category', models.CharField(blank=True, db_column='name', max_length=50, null=True)),
                ('rowguid', models.CharField(blank=True, max_length=100, null=True)),
                ('modifieddate', models.DateField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Detail',
            fields=[
                ('product_name', models.CharField(blank=True, max_length=50, null=True)),
                ('productid', models.IntegerField(blank=True, primary_key=True, serialize=False)),
                ('description', models.CharField(blank=True, max_length=5000, null=True)),
                ('quantity', models.IntegerField(blank=True, null=True)),
                ('listprice', models.DecimalField(decimal_places=4, max_digits=19)),
                ('is_available', models.CharField(blank=True, max_length=5, null=True)),
                ('images', models.CharField(blank=True, max_length=50, null=True)),
                ('category', models.CharField(blank=True, max_length=50, null=True)),
                ('modifieddate', models.DateField(blank=True, null=True)),
                ('productcategoryid', models.IntegerField(blank=True, null=True)),
                ('productsubcategoryid', models.IntegerField(blank=True, null=True)),
                ('subcategory', models.CharField(blank=True, max_length=50, null=True)),
                ('weight', models.FloatField(blank=True, null=True)),
                ('productline', models.CharField(blank=True, max_length=50, null=True)),
                ('class_field', models.CharField(blank=True, db_column='class', max_length=50, null=True)),
                ('style', models.CharField(blank=True, max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('subcategory', models.CharField(blank=True, max_length=50, null=True)),
                ('productsubcategoryid', models.CharField(blank=True, max_length=50, primary_key=True, serialize=False)),
                ('quantity', models.IntegerField(blank=True, null=True)),
                ('is_available', models.CharField(blank=True, max_length=5, null=True)),
                ('images', models.CharField(blank=True, max_length=50, null=True)),
                ('category', models.CharField(blank=True, max_length=50, null=True)),
                ('modifieddate', models.DateField(blank=True, null=True)),
                ('productcategoryid', models.IntegerField(blank=True, null=True)),
            ],
        ),
    ]
