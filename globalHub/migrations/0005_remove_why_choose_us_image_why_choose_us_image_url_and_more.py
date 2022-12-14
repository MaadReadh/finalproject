# Generated by Django 4.0.4 on 2022-06-18 02:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('globalHub', '0004_service_icon_url'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='why_choose_us',
            name='image',
        ),
        migrations.AddField(
            model_name='why_choose_us',
            name='image_url',
            field=models.TextField(default='globalHub/assets/images/reason-savetime.png'),
        ),
        migrations.AlterField(
            model_name='why_choose_us',
            name='descriptions',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='why_choose_us',
            name='title',
            field=models.CharField(max_length=60),
        ),
    ]
