# Generated by Django 2.1.4 on 2019-01-19 13:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0002_auto_20190114_1037'),
    ]

    operations = [
        migrations.CreateModel(
            name='Configuration',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('maxbooksonloan', models.PositiveIntegerField()),
            ],
        ),
    ]