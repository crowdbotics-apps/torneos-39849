# Generated by Django 2.2.28 on 2023-04-15 00:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('torneos', '0010_delete_jugadoresdisciplinas'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='torneos',
            name='formato',
        ),
        migrations.DeleteModel(
            name='Formatos',
        ),
    ]
