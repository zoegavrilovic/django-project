# Generated by Django 2.2.4 on 2019-09-03 22:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('approda', '0002_auto_20190904_0025'),
    ]

    operations = [
        migrations.AlterField(
            model_name='evidencijeprijema',
            name='sifra_artikla',
            field=models.ForeignKey(db_column='sifra_artikla', on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='approda.Artikli', unique=True),
        ),
    ]
