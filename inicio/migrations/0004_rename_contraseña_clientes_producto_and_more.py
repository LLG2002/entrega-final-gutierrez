# Generated by Django 4.2 on 2023-04-26 23:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inicio', '0003_rename_edad_clientes_telefono'),
    ]

    operations = [
        migrations.RenameField(
            model_name='clientes',
            old_name='contraseña',
            new_name='producto',
        ),
        migrations.AddField(
            model_name='clientes',
            name='conjunto',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
