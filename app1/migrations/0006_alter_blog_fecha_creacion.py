# Generated by Django 4.0.4 on 2022-06-01 22:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0005_alter_blog_fecha_creacion'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='fecha_creacion',
            field=models.TextField(default='2022-06-01 19:05:21.254999'),
        ),
    ]