# Generated by Django 3.1.1 on 2020-10-10 17:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stv', '0016_auto_20201010_1811'),
    ]

    operations = [
        migrations.AlterField(
            model_name='detail',
            name='es_far',
            field=models.CharField(default=0, max_length=15, verbose_name='اسکناس فرسوده'),
        ),
        migrations.AlterField(
            model_name='detail',
            name='ir_far',
            field=models.CharField(default=0, max_length=100, verbose_name='ایران چک فرسوده'),
        ),
        migrations.AlterField(
            model_name='detail',
            name='n_1',
            field=models.CharField(default=0, max_length=15, verbose_name='1000'),
        ),
        migrations.AlterField(
            model_name='detail',
            name='n_10',
            field=models.CharField(default=0, max_length=15, verbose_name='10000'),
        ),
        migrations.AlterField(
            model_name='detail',
            name='n_2',
            field=models.CharField(default=0, max_length=35, verbose_name='2000'),
        ),
        migrations.AlterField(
            model_name='detail',
            name='n_5',
            field=models.CharField(default=0, max_length=15, verbose_name='5000'),
        ),
        migrations.AlterField(
            model_name='detail',
            name='sek_n',
            field=models.CharField(default=0, max_length=15, verbose_name='سکه نیم'),
        ),
        migrations.AlterField(
            model_name='detail',
            name='sek_r',
            field=models.CharField(default=0, max_length=15, verbose_name='سکه ربع'),
        ),
        migrations.AlterField(
            model_name='detail',
            name='sek_t',
            field=models.CharField(default=0, max_length=15, verbose_name='سکه تمام'),
        ),
        migrations.AlterField(
            model_name='detail',
            name='t_ch_25',
            field=models.CharField(default=0, max_length=15, verbose_name='دسته چک 25'),
        ),
        migrations.AlterField(
            model_name='detail',
            name='t_ch_50',
            field=models.CharField(default=0, max_length=15, verbose_name='دسته جک 50'),
        ),
        migrations.AlterField(
            model_name='detail',
            name='t_ch_hav',
            field=models.CharField(default=0, max_length=15, verbose_name='دسته چک حواله'),
        ),
        migrations.AlterField(
            model_name='detail',
            name='t_ch_taz',
            field=models.CharField(default=0, max_length=15, verbose_name='دسته چک تضمین'),
        ),
        migrations.AlterField(
            model_name='detail',
            name='t_m',
            field=models.CharField(default=0, max_length=30, verbose_name='تمبرمالیاتی'),
        ),
        migrations.AlterField(
            model_name='detail',
            name='t_pard',
            field=models.CharField(default=0, max_length=15, verbose_name='دستور پرداخت'),
        ),
        migrations.AlterField(
            model_name='detail',
            name='t_saf',
            field=models.CharField(default=0, max_length=15, verbose_name='تمبرسفته'),
        ),
        migrations.AlterField(
            model_name='detail',
            name='t_va',
            field=models.CharField(default=0, max_length=15, verbose_name='تمبر واخواست'),
        ),
    ]
