# Generated by Django 5.0.3 on 2024-03-14 09:39

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('make', models.CharField(max_length=100)),
                ('model', models.CharField(blank=True, max_length=100)),
                ('year', models.CharField(max_length=4, null=True)),
                ('size_of_engine', models.CharField(choices=[('1000cm dan kichik', '1000cm dan kichik'), ('1001 - 3000cm gacha', '1001 - 3000cm gacha'), ('3000cm dan katta', '3000cm dan katta')], max_length=19)),
                ('country', models.CharField(choices=[('Rossiya', 'Rossiya'), ('Dubay', 'Dubay'), ('Xitoy', 'Xitoy')], max_length=20)),
                ('type_of_car', models.CharField(choices=[('Benzin-Dizel', 'Benzin-Dizel'), ('Elektr-Gibrid', 'Elektr-Gibrid')], max_length=20)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='TempUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_agent', models.CharField(max_length=50)),
                ('device_family', models.CharField(max_length=255)),
                ('device_brand', models.CharField(max_length=255, null=True)),
                ('device_model', models.CharField(max_length=255, null=True)),
                ('browser_family', models.CharField(max_length=255, null=True)),
                ('browser_version_string', models.CharField(max_length=255, null=True)),
                ('device_os_family', models.CharField(max_length=255, null=True)),
                ('device_os_version_string', models.CharField(max_length=255, null=True)),
                ('is_mobile', models.BooleanField(default=False)),
                ('is_tablet', models.BooleanField(default=False)),
                ('is_touch_capable', models.BooleanField(default=False)),
                ('is_pc', models.BooleanField(default=False)),
                ('is_bot', models.BooleanField(default=False)),
                ('ip_address', models.GenericIPAddressField()),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Temporary users',
            },
        ),
    ]
