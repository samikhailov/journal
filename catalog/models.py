import uuid

import mammoth
from django.db import models
from django.urls import reverse
from django.utils import timezone
from markdown import markdown

from catalog.tasks.pdf_gen import create_publication_cert, create_participation_cert


class Article(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    name = models.CharField(max_length=200, verbose_name='Название публикации')
    journal = models.ForeignKey('Journal', verbose_name='Журнал', on_delete=models.CASCADE)
    rubric = models.ForeignKey('Rubric', verbose_name='Рубрика', on_delete=models.CASCADE)
    contact_name = models.CharField(max_length=200, verbose_name='ФИО контактного лица')
    contact_email = models.EmailField(max_length=75, verbose_name='E-mail контактного лица')
    author = models.CharField(max_length=100, verbose_name='Автор')
    raw_article_file = models.FileField(upload_to='journal/articles', verbose_name='Оригинальный файл публикации')
    clean_article_file = models.FileField(upload_to='journal/articles', verbose_name='Обработанный файл публикации',
                                          blank=True)
    html_article_text = models.TextField(editable=False)
    pages = models.PositiveIntegerField(verbose_name='Количество страниц')
    comment = models.TextField(blank=True, verbose_name='Комментарий')
    is_published = models.BooleanField(default=True, verbose_name='Опубликовано')
    need_participation_cert = models.BooleanField(default=True, verbose_name='Создать сертефикат')
    publication_cert_link = models.CharField(max_length=500, verbose_name='Справка о публикации')
    participation_cert_link = models.CharField(max_length=500, verbose_name='Сертификат участника')
    created_date = models.DateField(default=timezone.now, verbose_name='Дата создания в UTC')

    def __str__(self):
        return '%s, %s' % (self.name, self.journal)

    def save(self):
        self.publication_cert_link = create_publication_cert(self.uuid, self.name, self.author, self.journal,
                                                             self.journal.publication_date,
                                                             self.created_date)
        if self.need_participation_cert is True:
            self.participation_cert_link = create_participation_cert(self.uuid, self.name, self.author, self.journal)
        super(Article, self).save()

        if self.clean_article_file.name is not '':
            with open(self.clean_article_file.path, "rb") as docx_file:
                result = mammoth.convert_to_html(docx_file)
                self.html_article_text = result.value
        else:
            self.html_article_text = ''

        super(Article, self).save()

    def get_absolute_url(self):
        return reverse('article-detail', args=[str(self.id)])

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'


class Rubric(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return '%s' % self.name

    class Meta:
        verbose_name = 'Рубрика'
        verbose_name_plural = 'Рубрики'


class Journal(models.Model):
    name = models.CharField(max_length=100, unique=True)
    deadline_date = models.DateField(null=True, blank=True)
    publication_date = models.DateField(null=True, blank=True)
    cover = models.ImageField(upload_to='journal/covers')
    issn = models.IntegerField()
    is_published = models.BooleanField(default=False)
    is_visible = models.BooleanField(default=False)

    def available_for_publication(self):
        from datetime import date
        if self.deadline_date >= date.today():
            return True
        else:
            return False

    def __str__(self):
        return '%s' % self.name

    def get_absolute_url(self):
        return reverse('journal-detail', args=[str(self.id)])

    class Meta:
        verbose_name = 'Журнал'
        verbose_name_plural = 'Журналы'
