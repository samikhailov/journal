from django import forms

from .models import Article


class ArticleCreateForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['name', 'journal', 'rubric', 'contact_name', 'contact_email', 'author', 'raw_article_file', 'pages',
                  'need_participation_cert', 'comment'
                  ]
