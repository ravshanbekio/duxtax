# Generated by Django 5.0.3 on 2024-03-25 12:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0009_remove_car_country_alter_car_type_of_car'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='price',
            field=models.PositiveIntegerField(),
        ),
        migrations.AlterField(
            model_name='car',
            name='size_of_engine',
            field=models.CharField(choices=[('1000cm dan kichik', '1000cm dan kichik'), ('1000cm dan katta', '1000cm dan katta')], max_length=19),
        ),
    ]
