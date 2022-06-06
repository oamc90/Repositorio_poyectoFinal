# Generated by Django 4.0.4 on 2022-06-06 15:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0008_blog_creador_alter_blog_fecha_creacion'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='imagen',
            field=models.ImageField(blank=True, null=True, upload_to='avatar'),
        ),
        migrations.AlterField(
            model_name='blog',
            name='fecha_creacion',
            field=models.TextField(default='2022-06-06 12:51:11.517341'),
        ),
    ]