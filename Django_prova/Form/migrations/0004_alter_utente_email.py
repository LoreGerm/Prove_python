# Generated by Django 4.0.3 on 2022-03-18 17:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Form', '0003_utente_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='utente',
            name='email',
            field=models.EmailField(max_length=100, null='false'),
        ),
    ]
