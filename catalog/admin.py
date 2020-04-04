from django.contrib import admin
from .models import Article, Journal, Rubric


admin.site.register(Rubric)


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('name', 'journal', 'pages')
    readonly_fields = ['created_date', 'publication_cert_link', 'participation_cert_link']


@admin.register(Journal)
class JournalAdmin(admin.ModelAdmin):
    list_display = ('name', 'deadline_date', 'publication_date', 'is_published', 'is_visible')
    list_filter = ('is_published', 'is_visible')
