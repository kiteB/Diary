# Generated by Django 3.2.5 on 2021-07-14 11:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('diary', '0002_alter_diary_pub_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='diary',
            name='pub_date',
            field=models.DateTimeField(),
        ),
    ]