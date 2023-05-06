# Generated by Django 3.2 on 2023-05-06 08:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Individual',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ghana_card_id', models.CharField(max_length=30, unique=True)),
                ('TIN_number', models.CharField(max_length=30, unique=True)),
                ('name_of_individual', models.CharField(max_length=100)),
                ('status', models.CharField(choices=[('MEMBER NOMINATED', 'Member Nominated'), ('INDEPENDENT', 'Independent')], max_length=30)),
            ],
        ),
    ]
