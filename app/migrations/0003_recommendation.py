# Generated by Django 4.2.7 on 2023-12-03 20:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_account_sp_department'),
    ]

    operations = [
        migrations.CreateModel(
            name='Recommendation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('recommendation_order', models.IntegerField()),
                ('score', models.FloatField()),
            ],
        ),
    ]
