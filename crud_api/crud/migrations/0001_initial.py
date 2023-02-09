# Generated by Django 2.2 on 2021-10-29 06:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Prod_Name', models.CharField(max_length=250)),
                ('Prod_Author', models.CharField(max_length=150)),
                ('Prod_Price', models.IntegerField()),
            ],
            options={
                'verbose_name': 'Product',
            },
        ),
    ]