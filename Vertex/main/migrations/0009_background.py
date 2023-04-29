# Generated by Django 4.2 on 2023-04-28 15:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_opinion'),
    ]

    operations = [
        migrations.CreateModel(
            name='BackGround',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img1', models.ImageField(upload_to='media', verbose_name='Image 1')),
                ('img2', models.ImageField(upload_to='media', verbose_name='Image 2')),
                ('img3', models.ImageField(upload_to='media', verbose_name='Image 3')),
                ('img4', models.ImageField(upload_to='media', verbose_name='Image 4')),
            ],
            options={
                'verbose_name': 'BackGround',
                'verbose_name_plural': 'BackGrounds',
            },
        ),
    ]