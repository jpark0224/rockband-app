# Generated by Django 4.0.4 on 2022-04-21 16:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0001_initial'),
        ('bands', '0005_band_active_alter_band_genres'),
    ]

    operations = [
        migrations.AddField(
            model_name='band',
            name='member',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='members.member'),
        ),
    ]