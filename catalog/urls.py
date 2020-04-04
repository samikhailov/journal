from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from . import views

urlpatterns = [
    path("", views.JournalListView.as_view(template_name="index.html"), name="index"),
    path("journals/", views.JournalListView.as_view(), name="journals"),
    path("journals/coming/", views.JournalListView.as_view(), name="journals-coming"),
    path("journals/archive/", views.JournalListView.as_view(), name="journals-archive"),
    path("journals/article/", views.ArticleListView.as_view(), name="articles"),
    path("journals/<int:pk>/", views.JournalDetailView.as_view(), name="journal-detail"),
    path("journals/<int:pk>/article/create/", views.ArticleCreate.as_view(), name="article_create"),
    path("journals/article/<int:pk>/", views.ArticleDetailView.as_view(), name="article-detail"),
    path("for-authors/", views.blank, name="for-authors"),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
