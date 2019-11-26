# Generated by Django 2.2.4 on 2019-09-03 22:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Artikli',
            fields=[
                ('sifra_artikla', models.BigIntegerField(primary_key=True, serialize=False)),
                ('naziv', models.CharField(max_length=15)),
                ('cena', models.IntegerField()),
                ('jedinica_mere', models.CharField(max_length=8)),
                ('rok_trajanja', models.DateField()),
            ],
            options={
                'db_table': 'artikli',
            },
        ),
        migrations.CreateModel(
            name='Dobavljaci',
            fields=[
                ('sifra_dobavljaca', models.IntegerField(primary_key=True, serialize=False)),
                ('naziv', models.CharField(max_length=20)),
            ],
            options={
                'db_table': 'dobavljaci',
            },
        ),
        migrations.CreateModel(
            name='Kupci',
            fields=[
                ('jmbg', models.BigIntegerField(primary_key=True, serialize=False)),
                ('ime', models.CharField(blank=True, max_length=15, null=True)),
                ('prezime', models.CharField(blank=True, max_length=20, null=True)),
                ('kartica', models.BigIntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'kupci',
            },
        ),
        migrations.CreateModel(
            name='Objekti',
            fields=[
                ('pib', models.IntegerField(primary_key=True, serialize=False)),
                ('naziv', models.CharField(max_length=20)),
                ('adresa', models.CharField(max_length=40)),
                ('grad', models.CharField(max_length=15)),
                ('broj_telefona', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'objekti',
            },
        ),
        migrations.CreateModel(
            name='Racuni',
            fields=[
                ('racunid', models.BigIntegerField(primary_key=True, serialize=False)),
                ('datum', models.DateField()),
                ('vreme', models.CharField(max_length=8)),
                ('ukupno', models.BigIntegerField()),
                ('kartica', models.BigIntegerField(blank=True, null=True)),
                ('jmbg', models.ForeignKey(db_column='jmbg', on_delete=django.db.models.deletion.CASCADE, to='approda.Kupci')),
            ],
            options={
                'db_table': 'racuni',
            },
        ),
        migrations.CreateModel(
            name='Otpremnice',
            fields=[
                ('sifra_otpremnice', models.BigIntegerField(primary_key=True, serialize=False)),
                ('datum_otpreme', models.DateField()),
                ('sifra_dobavljaca', models.ForeignKey(db_column='sifra_dobavljaca', on_delete=django.db.models.deletion.CASCADE, to='approda.Dobavljaci')),
            ],
            options={
                'db_table': 'otpremnice',
                'unique_together': {('sifra_otpremnice', 'sifra_dobavljaca')},
            },
        ),
        migrations.CreateModel(
            name='StavkeRacuna',
            fields=[
                ('kolicina', models.IntegerField()),
                ('sifra_artikla', models.ForeignKey(db_column='sifra_artikla', on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='approda.Artikli')),
                ('racunid', models.ForeignKey(db_column='racunid', on_delete=django.db.models.deletion.CASCADE, to='approda.Racuni')),
            ],
            options={
                'db_table': 'stavke_racuna',
                'unique_together': {('sifra_artikla', 'racunid')},
            },
        ),
        migrations.CreateModel(
            name='EvidencijePrijema',
            fields=[
                ('kolicina', models.IntegerField()),
                ('broj_kalkulacija', models.IntegerField(blank=True, null=True)),
                ('sifra_artikla', models.ForeignKey(db_column='sifra_artikla', on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='approda.Artikli')),
                ('naziv_objekta', models.CharField(max_length=20)),
                ('pib', models.ForeignKey(db_column='pib', on_delete=django.db.models.deletion.CASCADE, to='approda.Objekti')),
                ('sifra_dobavljaca', models.ForeignKey(db_column='sifra_dobavljaca', on_delete=django.db.models.deletion.CASCADE, related_name='otpremnice_sif_dob', to='approda.Otpremnice')),
                ('sifra_otpremnice', models.ForeignKey(db_column='sifra_otpremnice', on_delete=django.db.models.deletion.CASCADE, related_name='otpremnice_sif_otp', to='approda.Otpremnice')),
            ],
            options={
                'db_table': 'evidencije_prijema',
                'unique_together': {('sifra_artikla', 'pib', 'sifra_otpremnice', 'sifra_dobavljaca')},
            },
        ),
    ]
