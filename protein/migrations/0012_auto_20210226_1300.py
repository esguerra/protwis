# Generated by Django 3.0.2 on 2021-02-26 12:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0003_citation_page_name'),
        ('protein', '0011_proteinarrestinpair'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='proteinarrestinpair',
            name='references',
        ),
        migrations.AddField(
            model_name='proteinarrestinpair',
            name='publication',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='common.Publication'),
        ),
    ]
