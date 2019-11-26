# Generated by Django 2.2.5 on 2019-09-05 19:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('approda', '0006_auto_20190905_2106'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='stavkeracuna',
            name='id',
        ),
        migrations.AddField(
            model_name='evidencijeprijema',
            name='pk_evidencije_prijema',
            field=models.AutoField(auto_created=True, default=0, primary_key=True, serialize=False),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='stavkeracuna',
            name='pk_stavke_racuna',
            field=models.AutoField(auto_created=True, default=1, primary_key=True, serialize=False),
            preserve_default=False,
        ),
        migrations.AlterUniqueTogether(
            name='evidencijeprijema',
            unique_together={('sifra_artikla', 'pib', 'sifra_otpremnice')},
        ),
        migrations.RemoveField(
            model_name='evidencijeprijema',
            name='id',
        ),
        migrations.RemoveField(
            model_name='evidencijeprijema',
            name='sifra_dobavljaca',
        ),
    ]
