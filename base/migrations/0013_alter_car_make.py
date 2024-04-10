# Generated by Django 5.0.3 on 2024-04-10 17:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0012_tempuser_added_date_alter_car_result_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='make',
            field=models.CharField(choices=[('Tesla', 'Tesla'), ('Toyota', 'Toyota'), ('Ford', 'Ford'), ('Honda', 'Honda'), ('BMW', 'BMW'), ('Subaru', 'Subaru'), ('Hyundai', 'Hyundai'), ('Audi', 'Audi'), ('Jeep', 'Jeep'), ('Porsche', 'Porsche'), ('Dodge', 'Dodge'), ('Ferrari', 'Ferrari'), ('Jaguar', 'Jaguar'), ('Lamborghini', 'Lamborghini'), ('Maserati', 'Maserati'), ('Bentley', 'Bentley'), ('Chrysler', 'Chrysler'), ('Chevrolet', 'Chevrolet'), ('Cadillac', 'Cadillac'), ('Mazda', 'Mazda'), ('Nissan', 'Nissan'), ('Alfa Romeo', 'Alfa Romeo'), ('Bugatti', 'Bugatti'), ('Buick', 'Buick'), ('Lexus', 'Lexus'), ('Rolls-Royce', 'Rolls-Royce'), ('Acura', 'Acura'), ('Aston Martin', 'Aston Martin'), ('Kia', 'Kia'), ('Mercedes-Benz', 'Mercedes-Benz'), ('Volkswagen', 'Volkswagen'), ('Volvo', 'Volvo'), ('McLaren', 'McLaren'), ('Mitsubishi', 'Mitsubishi'), ('GMC', 'GMC'), ('Infiniti', 'Infiniti'), ('Lincoln', 'Lincoln'), ('Peugeot', 'Peugeot'), ('Pontiac', 'Pontiac'), ('Saab', 'Saab'), ('Genesis', 'Genesis'), ('Suzuki', 'Suzuki'), ('Citroën', 'Citroën'), ('Fiat', 'Fiat'), ('Lotus', 'Lotus'), ('Mini', 'Mini'), ('BYD', 'BYD'), ('Exeed', 'Exeed'), ('Jetour', 'Jetour'), ('Changan', 'Changan'), ('Geely', 'Geely'), ('Great Wall', 'Great Wall'), ('BAIC', 'BAIC'), ('Dongfeng', 'Dongfeng'), ('FAW', 'FAW'), ('GAC', 'GAC'), ('SAIC', 'SAIC'), ('Chery', 'Chery'), ('JAC', 'JAC')], max_length=100),
        ),
    ]
