# Generated by Django 4.0.4 on 2022-06-18 02:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('globalHub', '0005_remove_why_choose_us_image_why_choose_us_image_url_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact_us',
            name='facebook_url',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='contact_us',
            name='instagram_url',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='contact_us',
            name='telegram_url',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='about_us',
            name='text',
            field=models.TextField(),
        ),
    ]
