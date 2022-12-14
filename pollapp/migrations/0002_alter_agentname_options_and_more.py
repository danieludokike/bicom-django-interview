# Generated by Django 4.1.4 on 2022-12-14 06:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pollapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='agentname',
            options={'managed': False},
        ),
        migrations.AlterModelOptions(
            name='announcedlgaresults',
            options={'managed': False},
        ),
        migrations.AlterModelOptions(
            name='announcedpuresults',
            options={'managed': False},
        ),
        migrations.AlterModelOptions(
            name='announcedstateresults',
            options={'managed': False},
        ),
        migrations.AlterModelOptions(
            name='announcedwardresults',
            options={'managed': False},
        ),
        migrations.AlterModelOptions(
            name='lga',
            options={'managed': False},
        ),
        migrations.AlterModelOptions(
            name='party',
            options={'managed': False},
        ),
        migrations.AlterModelOptions(
            name='pollingunit',
            options={'managed': False},
        ),
        migrations.AlterModelOptions(
            name='states',
            options={'managed': False},
        ),
        migrations.AlterField(
            model_name='ward',
            name='date_entered',
            field=models.CharField(max_length=50),
        ),
    ]