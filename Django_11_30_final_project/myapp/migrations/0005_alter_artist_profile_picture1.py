# Generated by Django 4.2.4 on 2023-09-05 06:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_artist_profile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='artist_profile',
            name='picture1',
            field=models.ImageField(default='default.png', upload_to='artist_pic/'),
        ),
    ]
