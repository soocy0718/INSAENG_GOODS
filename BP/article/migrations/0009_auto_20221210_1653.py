# Generated by Django 3.2 on 2022-12-10 07:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0008_alter_post_board_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='Board_gtype',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='Board_title',
            field=models.CharField(max_length=250),
        ),
    ]
