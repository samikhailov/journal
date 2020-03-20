# Generated by Django 2.0.13 on 2020-03-20 14:49

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('name', models.CharField(max_length=200, verbose_name='Название публикации')),
                ('contact_name', models.CharField(max_length=200, verbose_name='ФИО контактного лица')),
                ('contact_email', models.EmailField(max_length=75, verbose_name='E-mail контактного лица')),
                ('author', models.CharField(max_length=100, verbose_name='Автор')),
                ('raw_article_file', models.FileField(upload_to='journal/articles', verbose_name='Оригинальный файл публикации')),
                ('clean_article_file', models.FileField(blank=True, upload_to='journal/articles', verbose_name='Обработанный файл публикации')),
                ('html_article_text', models.TextField(editable=False)),
                ('pages', models.PositiveIntegerField(verbose_name='Количество страниц')),
                ('comment', models.TextField(blank=True, verbose_name='Комментарий')),
                ('is_published', models.BooleanField(default=True, verbose_name='Опубликовано')),
                ('need_participation_cert', models.BooleanField(default=True, verbose_name='Создать сертефикат')),
                ('publication_cert_link', models.CharField(max_length=500, verbose_name='Справка о публикации')),
                ('participation_cert_link', models.CharField(max_length=500, verbose_name='Сертификат участника')),
                ('created_date', models.DateField(default=django.utils.timezone.now, verbose_name='Дата создания в UTC')),
            ],
            options={
                'verbose_name': 'Статья',
                'verbose_name_plural': 'Статьи',
            },
        ),
        migrations.CreateModel(
            name='Journal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('deadline_date', models.DateField(blank=True, null=True)),
                ('publication_date', models.DateField(blank=True, null=True)),
                ('cover', models.ImageField(upload_to='journal/covers')),
                ('issn', models.IntegerField()),
                ('is_published', models.BooleanField(default=False)),
                ('is_visible', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': 'Журнал',
                'verbose_name_plural': 'Журналы',
            },
        ),
        migrations.CreateModel(
            name='Page',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('private_title', models.CharField(max_length=100)),
                ('public_title', models.CharField(max_length=100)),
                ('content', models.TextField()),
                ('html_content', models.TextField(editable=False)),
            ],
            options={
                'verbose_name': 'Страница',
                'verbose_name_plural': 'Страницы',
            },
        ),
        migrations.CreateModel(
            name='Rubric',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
            ],
            options={
                'verbose_name': 'Рубрика',
                'verbose_name_plural': 'Рубрики',
            },
        ),
        migrations.AddField(
            model_name='article',
            name='journal',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalog.Journal', verbose_name='Журнал'),
        ),
        migrations.AddField(
            model_name='article',
            name='rubric',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalog.Rubric', verbose_name='Рубрика'),
        ),
    ]
