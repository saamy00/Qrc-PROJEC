# Generated by Django 5.1.1 on 2024-10-08 07:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0003_background_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='background_image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='background images')),
            ],
        ),
        migrations.DeleteModel(
            name='background',
        ),
    ]
