# Generated by Django 4.0.3 on 2022-05-04 13:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='myuser',
            name='route',
        ),
        migrations.AddField(
            model_name='route',
            name='id_vehicle',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='main.transport'),
        ),
        migrations.AddField(
            model_name='route',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]