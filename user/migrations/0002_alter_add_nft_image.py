# Generated by Django 4.1.1 on 2023-05-29 11:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='add_nft',
            name='image',
            field=models.ImageField(default='', upload_to='static/images'),
        ),
    ]
