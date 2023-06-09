# Generated by Django 4.1.1 on 2023-05-29 11:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Add_nft',
            fields=[
                ('nft_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('category', models.CharField(default='', max_length=50)),
                ('price', models.CharField(default='', max_length=50)),
                ('desc', models.CharField(default='', max_length=300)),
                ('phone', models.CharField(default='', max_length=111)),
                ('image', models.ImageField(default='', upload_to='resale/images')),
                ('nft_name', models.CharField(default='', max_length=300)),
            ],
        ),
    ]
