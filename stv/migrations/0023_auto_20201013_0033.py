# Generated by Django 3.1.1 on 2020-10-12 21:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('stv', '0022_auto_20201013_0003'),
    ]

    operations = [
        migrations.AlterField(
            model_name='detail',
            name='branch',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='branch_user', to=settings.AUTH_USER_MODEL, verbose_name='شعبه'),
        ),
    ]
