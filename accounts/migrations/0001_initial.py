# Generated by Django 2.1.5 on 2019-08-26 20:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_countries.fields
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('description', models.TextField(max_length=250)),
                ('address', models.CharField(max_length=50)),
                ('phone_number', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None)),
                ('checkup_price', models.DecimalField(blank=True, decimal_places=2, max_digits=4, null=True)),
                ('city', models.CharField(max_length=20)),
                ('photo', models.ImageField(blank=True, upload_to='uploads')),
                ('country', django_countries.fields.CountryField(blank=True, max_length=2)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profile', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
