# Generated by Django 4.2 on 2023-06-03 20:01

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inicio', '0011_alter_clientes_fecha_de_realizacion'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clientes',
            name='descripcion',
            field=ckeditor.fields.RichTextField(null=True),
        ),
    ]
