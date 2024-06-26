from django.db import models
from django.utils.translation import gettext_lazy as _


class Category(models.Model):
    parent = models.ForeignKey('self', verbose_name=_('parent'), on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(verbose_name=_('title'), max_length=50)
    description = models.TextField(verbose_name=_('description'), blank=True)
    avatar = models.ImageField(verbose_name=_('avatar'), upload_to='categories/', blank=True)
    is_enable = models.BooleanField(verbose_name=_('is enable'), default=True)
    created_time = models.DateTimeField(auto_now_add=True, verbose_name=_('created at'))
    updated_time = models.DateTimeField(auto_now=True, verbose_name=_('updated at'))

    class Meta:
        db_table = 'categories'
        verbose_name = _('Category')
        verbose_name_plural = _('Categories')

    def __str__(self):
        return self.title


class Product(models.Model):
    title = models.CharField(verbose_name=_('title'), max_length=50)
    description = models.TextField(verbose_name=_('description'), blank=True)
    avatar = models.ImageField(verbose_name=_('avatar'), upload_to='products/', blank=True)
    is_enable = models.BooleanField(verbose_name=_('is enable'), default=True)
    categories = models.ManyToManyField('Category', verbose_name=_('categories'), blank=True)
    created_time = models.DateTimeField(auto_now_add=True, verbose_name=_('created at'))
    updated_time = models.DateTimeField(auto_now=True, verbose_name=_('updated at'))

    class Meta:
        db_table = 'products'
        verbose_name = _('Product')
        verbose_name_plural = _('Products')

    def __str__(self):
        return self.title


class File(models.Model):
    FILE_AUDIO = 1
    FILE_VIDEO = 2
    FILE_PDF = 3
    FILE_TYPES = (
        (FILE_AUDIO, _('audio')),
        (FILE_VIDEO, _('video')),
        (FILE_PDF, _('pdf')),
    )

    product = models.ForeignKey('Product', verbose_name=_('product'), related_name='files', on_delete=models.CASCADE)
    title = models.CharField(verbose_name=_('title'), max_length=50)
    file_type = models.PositiveSmallIntegerField(choices=FILE_TYPES, verbose_name=_('file type'))
    file = models.FileField(verbose_name=_('file'), upload_to='files/%Y/%m/%d')
    is_enable = models.BooleanField(verbose_name=_('is enable'), default=True)
    created_time = models.DateTimeField(auto_now_add=True, verbose_name=_('created at'))
    updated_time = models.DateTimeField(auto_now=True, verbose_name=_('updated at'))

    class Meta:
        db_table = 'files'
        verbose_name = _('File')
        verbose_name_plural = _('Files')

    def __str__(self):
        return self.title