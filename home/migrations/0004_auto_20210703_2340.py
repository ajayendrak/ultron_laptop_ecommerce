# Generated by Django 3.2.3 on 2021-07-03 18:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_contactinfo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactinfo',
            name='date',
            field=models.DateField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='contactinfo',
            name='desc',
            field=models.TextField(),
        ),
        migrations.AlterModelTable(
            name='contactinfo',
            table='contactinfo',
        ),
    ]