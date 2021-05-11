# Generated by Django 3.1.1 on 2020-09-29 16:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('stv', '0002_auto_20200929_0050'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cash',
            name='inventory',
        ),
        migrations.RemoveField(
            model_name='cash',
            name='peyment',
        ),
        migrations.RemoveField(
            model_name='cash',
            name='recive',
        ),
        migrations.AddField(
            model_name='branch',
            name='ip',
            field=models.GenericIPAddressField(default='17.20.0.0'),
        ),
        migrations.AddField(
            model_name='cash',
            name='inventory_end_day',
            field=models.PositiveBigIntegerField(default=0, verbose_name='موجودی صندوق'),
        ),
        migrations.AddField(
            model_name='cash',
            name='peymen_day',
            field=models.PositiveBigIntegerField(default=0, verbose_name='پرداختی امروز'),
        ),
        migrations.AddField(
            model_name='cash',
            name='recive_day',
            field=models.PositiveBigIntegerField(default=0, verbose_name='دریافتی امروز'),
        ),
        migrations.AlterField(
            model_name='pricing',
            name='price',
            field=models.PositiveBigIntegerField(verbose_name='قیمت'),
        ),
        migrations.CreateModel(
            name='detail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total', models.PositiveBigIntegerField(verbose_name='مبلغ کل')),
                ('publish', models.DateTimeField(default=django.utils.timezone.now, verbose_name='تاریخ ثبت')),
                ('author', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='detailes', to=settings.AUTH_USER_MODEL, verbose_name='نویسنده')),
                ('branch', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='detailes', to='stv.branch', verbose_name='شعبه')),
                ('princing', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='detailes2', to='stv.pricing', verbose_name='سرفصل')),
            ],
            options={
                'verbose_name': 'جزئیات',
                'verbose_name_plural': 'همه جزئیات صندوق',
            },
        ),
    ]
