# Generated by Django 4.0.2 on 2022-02-25 15:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='images',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=255)),
                ('product_price', models.IntegerField()),
                ('image', models.ImageField(null=True, upload_to='image/')),
            ],
        ),
    ]
