from django.db import models
from django.utils import timezone
from extensions.utils import jalali_converter_date
from account.models import User
from django_jalali.db import models as jmodels
from jdatetime import datetime, timedelta


class DetailManager(models.Manager):

    def getDate(self):
        return self.filter(date_persian=datetime.today() - timedelta(days=1))


class Category(models.Model):
    title = models.CharField(max_length=100, verbose_name='سرفصل')
    slug = models.SlugField(max_length=100, unique=True, verbose_name='آدرس سرفصل')
    status = models.BooleanField(default=True, verbose_name='وضعیت نمایش')
    position = models.IntegerField(verbose_name='جایگاه')

    class Meta:
        verbose_name = 'دسته بندی صندوق'
        verbose_name_plural = 'اقلام صندوق'
        ordering = ['position']

    def __str__(self):
        return self.title

    # objects = CategoryManager()


class Pricing(models.Model):
    STATUS_CHOICES = (
        ('a', '1'),
        ('b', '25'),
        ('c', '50'),
        ('d', '100')
    )
    category = models.ForeignKey('Category', verbose_name='سرفصل', on_delete=models.SET_NULL, null=True,
                                 related_name='pricing')
    title = models.CharField(max_length=100, verbose_name='زیرمجموعه')
    price = models.PositiveBigIntegerField(verbose_name='قیمت')
    position = models.IntegerField(verbose_name='جایگاه')
    count = models.CharField(max_length=1, choices=STATUS_CHOICES, verbose_name='تعداد هر بسته')
    slug = models.SlugField(max_length=100, default='', null=False, unique=True, verbose_name='آدرس')
    status = models.BooleanField(default=True, verbose_name='وضعیت نمایش')

    class Meta:
        verbose_name = 'قیمت گذاری'
        verbose_name_plural = 'قیمت ها'
        ordering = ['position']

    def __str__(self):
        return self.title


class Branch(models.Model):
    profil = models.OneToOneField(User, null=True, on_delete=models.SET_NULL, related_name='profil_branch',
                                  verbose_name='نویسنده')
    branchId = models.CharField(max_length=10, unique=True, blank=False, null=False, verbose_name='کد شعبه')
    name = models.CharField(max_length=100, unique=True, blank=False, null=False, verbose_name='نام شعبه')
    tel1 = models.CharField(max_length=20, blank=True, default='', verbose_name='تلفن 1')
    tel2 = models.CharField(max_length=20, blank=True, default='', verbose_name='تلفن 2')
    manager = models.CharField(max_length=100, blank=True, default='رئیس شعبه', verbose_name='نام رییس')
    ip = models.GenericIPAddressField(default='17.20.0.0', verbose_name='آی پی شعبه')
    slug = models.SlugField(max_length=100, default='', null=False, unique=True, verbose_name='آدرس')
    status = models.BooleanField(default=True, verbose_name='وضعیت نمایش')

    class Meta:
        verbose_name = 'شعبه'
        verbose_name_plural = 'شعبه ها'

    def __str__(self):
        return self.name


class Cash(models.Model):
    objects = jmodels.jManager()
    branch = models.ForeignKey(User, null=True, on_delete=models.SET_NULL, related_name='author_detail',
                               verbose_name='نویسنده')
    recive_day = models.PositiveBigIntegerField(verbose_name='دریافتی امروز', default=0)
    peymen_day = models.PositiveBigIntegerField(verbose_name='پرداختی امروز', default=0)
    inventory_end_day = models.PositiveBigIntegerField(verbose_name='موجودی صندوق', default=0)
    publish = models.DateTimeField(default=timezone.now, verbose_name='تاریخ ثبت')
    date_persian = jmodels.jDateField(verbose_name='تاریخ شمسی', auto_now=True)

    class Meta:
        verbose_name = 'صندوق'
        verbose_name_plural = 'تاریخچه صندوق'

    def jpublish(self):
        return jalali_converter_date(self.publish)

    jpublish.short_description = 'تاریخ ثبت'


class Detail(models.Model):
    objects = jmodels.jManager()
    branch = models.ForeignKey(User, null=True, on_delete=models.SET_NULL, related_name='branch_user',
                               verbose_name='شعبه')
    ip = models.CharField(max_length=20, blank=True, null=True, verbose_name='ip')
    publish = models.DateTimeField(default=timezone.now, verbose_name='تاریخ ثبت')
    lastDateEdit = models.DateTimeField(default=timezone.now, verbose_name='زمان ویرایش')
    date_persian = jmodels.jDateField(verbose_name='تاریخ شمسی')
    es_1 = models.CharField(max_length=50, verbose_name='اسکناس 1000', default=0)
    es_2 = models.CharField(max_length=50, verbose_name='اسکناس 2000', default=0)
    es_5 = models.CharField(max_length=50, verbose_name='اسکناس 5000', default=0)
    es_10 = models.CharField(max_length=50, verbose_name='اسکناس 10000', default=0)
    es_20 = models.CharField(max_length=50, verbose_name='اسکناس 20000', default=0)
    es_50 = models.CharField(max_length=50, verbose_name='اسکناس 50000', default=0)
    es_100 = models.CharField(max_length=50, verbose_name='اسکناس 100000', default=0)
    es_far = models.CharField(max_length=50, verbose_name='اسکناس فرسوده', default=0)
    n_1 = models.CharField(max_length=50, verbose_name='نیکل 1000', default=0)
    n_2 = models.CharField(max_length=50, verbose_name='نیکل 2000', default=0)
    n_5 = models.CharField(max_length=50, verbose_name='نیکل 5000', default=0)
    n_10 = models.CharField(max_length=50, verbose_name='نیکل 10000', default=0)
    n_li = models.CharField(max_length=50, verbose_name='نیکل 10000', default=0)
    ir_50 = models.CharField(max_length=100, verbose_name='ایران چک 50', default=0)
    ir_100 = models.CharField(max_length=100, verbose_name='ایران چک 100', default=0)
    ir_far = models.CharField(max_length=100, verbose_name='ایران چک فرسوده', default=0)
    t_m = models.CharField(max_length=50, verbose_name='تمبرمالیاتی', default=0)
    t_va = models.CharField(max_length=50, verbose_name='تمبر واخواست', default=0)
    t_ch_25 = models.CharField(max_length=50, verbose_name='دسته چک 25', default=0)
    t_ch_50 = models.CharField(max_length=50, verbose_name='دسته چک 50', default=0)
    t_ch_100 = models.CharField(max_length=50, verbose_name='دسته چک 100', default=0)
    t_ch_hav = models.CharField(max_length=50, verbose_name='دسته چک حواله', default=0)
    t_ch_taz = models.CharField(max_length=50, verbose_name='دسته چک تضمین', default=0)
    t_pard = models.CharField(max_length=50, verbose_name='دستور پرداخت', default=0)
    t_saf = models.CharField(max_length=50, verbose_name='تمبرسفته', default=0)
    sek_t = models.CharField(max_length=50, verbose_name='سکه تمام', default=0)
    sek_n = models.CharField(max_length=50, verbose_name='سکه نیم', default=0)
    sek_r = models.CharField(max_length=50, verbose_name='سکه ربع', default=0)
    daryaft = models.CharField(max_length=100, default=0, verbose_name='دریافتی امروز')
    pardakht = models.CharField(max_length=100, default=0, verbose_name='پرداختی امروز')
    total_yesterday = models.CharField(max_length=100, default=0, blank=True, null=True, verbose_name='مانده دیروز')
    total = models.CharField(max_length=100, default=0, verbose_name='مانده صندوق')

    class Meta:
        verbose_name = 'جزئیات'
        verbose_name_plural = 'همه جزئیات صندوق'

    def jpublish(self):
        return jalali_converter_date(self.publish)

    jpublish.short_description = 'تاریخ ثبت'

    objects = DetailManager()
