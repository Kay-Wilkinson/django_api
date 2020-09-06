# Generated by Django 3.1.1 on 2020-09-04 09:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FoodMenuItems',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('food_item_name', models.CharField(max_length=60)),
                ('food_item_description', models.CharField(max_length=120)),
                ('food_item_price', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
    ]
